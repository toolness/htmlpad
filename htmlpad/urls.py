from django.conf.urls import patterns, include, url

PAD_NAME = '(?P<name>[A-Za-z\-0-9]+)'
MAYBE_PAD_EXT = '(?P<ext>\.(css|js|html|txt))?'
MAYBE_REV = '(/rev\.(?P<rev>[0-9]+))?'

RENDER_PAD = '%s%s%s' % (PAD_NAME, MAYBE_PAD_EXT, MAYBE_REV)

urlpatterns = patterns('htmlpad.views',
    url(r'^$', 'index', name='htmlpad-index'),
    (r'^%s$' % RENDER_PAD, 'add_trailing_slash'),
    url(r'^%s\/$' % RENDER_PAD, 'render_pad', name='render-pad'),
    url(r'^%s\/edit$' % PAD_NAME, 'edit_pad', name='edit-pad'),
)
