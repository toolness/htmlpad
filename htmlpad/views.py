# Create your views here.

import mimetypes

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from . import etherpad

def ctx(request, options=None):
    if not options:
        options = {}
    options.update({
        'request': request,
        'HTMLPAD_ROOT': settings.HTMLPAD_ROOT,
        'STATIC_URL': settings.STATIC_URL
    })
    return options

def index(request):
    holder = 'blarg'
    return render_to_response('htmlpad/index.html', ctx(request, {
        'edit_pad_template': reverse('edit-pad', kwargs={'name': holder}),
        'ep_arg': holder
    }))

def add_trailing_slash(request, **kwargs):
    return redirect('%s/' % request.path)

def edit_pad(request, name):
    return render_to_response('htmlpad/edit.html', ctx(request, {
        'render_pad_url': reverse('render-pad', kwargs={'name': name}),
        'etherpad_url': etherpad.get_edit_url(name),
        'name': name
    }))

def render_pad(request, name, ext, rev):
    resp = etherpad.get_raw_contents(name, rev)

    if resp.status == 200:
        if not ext:
            ext = '.html'
        mimetype = '%s; charset=utf-8' % mimetypes.types_map[ext]
        return HttpResponse(resp.read(), mimetype=mimetype)
    elif resp.status == 404:
        return render_to_response('htmlpad/404.html', ctx(request, {
            'edit_pad_url': reverse('edit-pad', kwargs={'name': name}),
            'name': name
        }))

    # TODO: Handle other cases, including etherpad timeouts,
    # server errors, etc.
