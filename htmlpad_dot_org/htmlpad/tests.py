from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from . import etherpad

class HtmlpadTests(TestCase):
    def test_index_page_works(self):
        c = Client()
        response = c.get('/%s' % settings.HTMLPAD_ROOT)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Welcome to' in response.content)

class EtherpadTests(TestCase):
    def test_get_edit_url(self):
        self.assertEqual(etherpad.get_edit_url('u'),
                         '%s://%s/u' % (settings.ETHERPAD_PROTOCOL,
                                        settings.ETHERPAD_HOST))
