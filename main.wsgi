#! /usr/bin/env python

import re
import httplib

pad_re = re.compile(r'^/([A-Za-z\-0-9]+)$')
pad_rev_re = re.compile(r'^/([A-Za-z\-0-9]+)/rev\.([0-9]+)$')

pad_server = "etherpad.mozilla.org:9000"
pad_text_url = "/ep/pad/export/%s/latest?format=txt"
pad_rev_text_url = "/ep/pad/export/%s/rev.%d?format=txt"

# Also see PAD_SQLMETA for info on most recent changes to etherpad docs.

def application(environ, start_response):
    match = pad_re.match(environ['PATH_INFO'])
    if match is None:
        match = pad_rev_re.match(environ['PATH_INFO'])
    if match is None:
        start_response('404 Not Found',
                       [('Content-Type', 'text/plain')])
        return ['Not Found']
    matches = match.groups()
    path = matches[0]
    if len(matches) > 1:
        urlpath = pad_rev_text_url % (path, int(matches[1]))
    else:
        urlpath = pad_text_url % path
    conn = httplib.HTTPConnection(pad_server)
    conn.request("GET", urlpath)
    resp = conn.getresponse()
    if resp.status == 200:
        start_response('200 OK',
                       [('Content-Type', 'text/html; '
		       			 'charset=utf-8')])
        return [resp.read()]
    else:
        start_response('404 Not Found',
                       [('Content-Type', 'text/plain')])
        return ['pad does not exist: %s' % path]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 8000
    httpd = make_server('127.0.0.1', port, application)
    print "Serving on port %d" % port
    httpd.serve_forever()
