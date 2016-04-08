import httplib

from django.conf import settings

PAD_TEXT_URL = "/p/%s/export/txt"
PAD_REV_TEXT_URL = "/p/%s/%d/export/txt"

protocols = dict(https=httplib.HTTPSConnection,
                 http=httplib.HTTPConnection)

def _get_url(urlpath):
    conn = protocols[settings.ETHERPAD_PROTOCOL](settings.ETHERPAD_HOST)
    conn.request("GET", urlpath)
    return conn.getresponse()

def get_edit_url(name):
    return '%s://%s/p/%s?useMonospaceFont=true' % (settings.ETHERPAD_PROTOCOL,
                           settings.ETHERPAD_HOST, name)

def get_raw_contents(name, rev=None):
    if rev:
        urlpath = PAD_REV_TEXT_URL % (name, int(rev))
    else:
        urlpath = PAD_TEXT_URL % name

    return _get_url(urlpath)
