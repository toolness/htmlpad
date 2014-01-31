# manage adds more directories to the Python path.
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import manage

import django.core.handlers.wsgi
from dj_static import Cling

application = Cling(django.core.handlers.wsgi.WSGIHandler())
