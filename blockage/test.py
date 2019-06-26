from nose.plugins import PluginTester
from blockage.plugins import MockHTTPCall, NoseBlockage
import requests
import unittest


class TestBlockage (PluginTester, unittest.TestCase):
    activate = '--with-blockage'
    plugins = [NoseBlockage()]

    def test_web_request(self):
        """Ensure web requests are blocked when this plugin is active."""

        with self.assertRaises(MockHTTPCall):
            requests.get('http://www.google.com')

    def makeSuite(self):
        # This will raise a not implemented error unless we override the
        # abstract subclass
        pass
