import os
import site

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

# Add the app dir to the python path so we can import manage.
site.addsitedir(path('..', 'htmlpad_dot_org'))

# manage adds more directories to the Python path.
import manage

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
