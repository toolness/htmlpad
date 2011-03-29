import re
import httplib
import mimetypes

# TODO: I think it's actually possible to create illegal URLs with this regexp, like
# /foo/rev.34/edit, which is impossible.
pad_re = re.compile(r'^/(?P<name>[A-Za-z\-0-9]+)(?P<ext>\.(css|js|html|txt))?(/rev\.(?P<rev>[0-9]+))?(?P<edit>/edit)?(?P<trailing_slash>|/)?$')

pad_text_url = "/ep/pad/export/%s/latest?format=txt"
pad_rev_text_url = "/ep/pad/export/%s/rev.%d?format=txt"

EDIT_TEMPLATE = """\
<!DOCTYPE html>
<meta charset="utf-8">
<title>Edit Pad: %(name)s</title>
<style>
body {
    font-family: Baskerville, serif;
    width: 1024px;
    margin: 0 auto;
}

a:hover {
    background: #f0f0f0;
}

iframe#etherpad {
    border: none;
    padding-left: 10px;
    float: right;
}

</style>
<script src="/jquery.js"></script>
<iframe id="etherpad" width="720" src="%(edit_pad_url)s"></iframe>

<div class="instructions"><p>Edit the pad on the right to build your HTML page (click the <em>Create Pad</em> button if necessary). Here's a simple page you can copy-and-paste into the pad to get started:</p>
<pre>&lt;!DOCTYPE html&gt;
&lt;meta charset="utf-8"&gt;
&lt;title&gt;My First Web Page&lt;/title&gt;
&lt;p&gt;Here is my first Web page!&lt;/p&gt;</pre> 
<p>Once you've written something, you can view your page at <a id="view" href="%(view_pad_url)s" target="view">%(hostname)s%(view_pad_url)s</a>.</p>
<p>Saving happens automatically, so don't worry about that.</p>
<p>Keep switching back and forth between the editor and the view to rapidly iterate on your design. Give the editor link to a friend if you'd like to collaborate in real-time! 
</p></div>


<script>
function resize() {
    $("#etherpad").height($(window).height() - 32);
}

$(window).resize(resize);
$(window).ready(resize);
</script>
"""

NOT_FOUND_TEMPLATE = """\
<!DOCTYPE html>
<meta charset="utf-8">
<style>
body {
    font-family: Baskerville, serif;
    width: 30em;
    margin: 0 auto;
}

a:hover {
    background: #f0f0f0;
}
</style>
<title>Pad %(name)s not found!</title>
<h1>Alas.</h1>
<p>The pad <code>%(name)s</code> doesn't exist yet, but you can create it by visiting <a target="edit" href="%(pad_url)s">%(hostname)s%(pad_url)s</a>. For more help, visit <a href="/">%(hostname)s</a>.</p>
"""

# Also see PAD_SQLMETA for info on most recent changes to etherpad docs.

def application(environ, start_response):
    pad_server = environ['htmlpad.etherpad']
    path = environ['PATH_INFO']
    if path == '/':
        path = "/instructions/"
    if path == '/jquery.js':
        start_response('302 Moved Temporarily',
                       [('Location', 'static-files/jquery.js')])
        return []
    match = pad_re.match(path)
    if match is None:
        start_response('404 Not Found',
                       [('Content-Type', 'text/plain')])
        return ['Not Found']
    padname = match.group('name')
    has_trailing_slash = match.group('trailing_slash')
    ext = match.group('ext')
    urlpath = pad_text_url % padname
    edit_pad_url = "http://%s/%s" % (pad_server, padname)
    if match.group('rev') is not None:
        urlpath = pad_rev_text_url % (padname,
                                      int(match.group('rev')))
    elif match.group('edit') is not None:
        #start_response('302 Found', [('Location', edit_pad_url)])
        edit_page = EDIT_TEMPLATE % {
            'name': padname,
            'edit_pad_url': edit_pad_url,
            'view_pad_url': '/%s/' % padname,
            'hostname': environ['HTTP_HOST']
        }
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return [edit_page]
    elif ext is None and not has_trailing_slash:
        start_response('302 Found', [('Location', '%s/' % path)])
        return []
    conn = httplib.HTTPConnection(pad_server)
    conn.request("GET", urlpath)
    resp = conn.getresponse()
    if resp.status == 200:
        if ext is not None:
            mimetype = mimetypes.types_map[ext]
        else:
            mimetype = 'text/html'

        mimetype = '%s; charset=utf-8' % mimetype
        start_response('200 OK', [('Content-Type', mimetype)])
        return [resp.read()]
    else:
        failtext = NOT_FOUND_TEMPLATE % {
          'name': padname,
          'pad_url': '/%s/edit' % padname,
          'hostname': environ['HTTP_HOST']
        }
        # Add some padding so Google Chrome doesn't override our
        # 404 with its own.
        failtext += (" " * 512)
        start_response('404 Not Found',
                       [('Content-Type', 'text/html')])
        return [failtext]
