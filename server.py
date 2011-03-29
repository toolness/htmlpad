import os
import sys
from wsgiref.simple_server import make_server
from wsgiref.util import shift_path_info, FileWrapper
from mimetypes import guess_type

sys.path.append(os.path.join('htmlpad.org', 'wsgi-scripts'))

import htmlpad

def error_404(env, start):
    return error(env, start, '404 Not Found', 
                 'Not Found: %s' % env['PATH_INFO'])

def static_file(env, start, static_files_dir):
    filename = env['PATH_INFO']
    if filename.endswith('/'):
        filename = '%sindex.html' % filename
    fileparts = filename[1:].split('/')
    fullpath = os.path.join(static_files_dir, *fileparts)
    fullpath = os.path.normpath(fullpath)
    (mimetype, encoding) = guess_type(fullpath)
    if (fullpath.startswith(static_files_dir) and
        not '.git' in fullpath and
        os.path.isfile(fullpath) and
        mimetype):
        filesize = os.stat(fullpath).st_size
        start('200 OK', [('Content-Type', mimetype),
                         ('Content-Length', str(filesize))])
        return FileWrapper(open(fullpath, 'rb'))
    return error_404(env, start)

def application(env, start):
    env['htmlpad.etherpad'] = 'etherpad.mozilla.org:9000'
    static_files_dir = os.path.join('htmlpad.org', 'static-files')
    
    if env['PATH_INFO'].startswith('/static-files/'):
        shift_path_info(env)
        return static_file(env, start, static_files_dir)
    else:
        return htmlpad.application(env, start)

if __name__ == '__main__':
    port = 8000

    print "serving on port %d" % port
    httpd = make_server('', port, application)
    httpd.serve_forever()
