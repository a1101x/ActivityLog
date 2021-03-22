from django.http import HttpRequest
from django.test import TestCase

from activitylogs.middleware import ActivityLogMiddleware


class ActivityLogMiddlewareTests(TestCase):

    def setUp(self):
        self.middleware = ActivityLogMiddleware()
        self.request = HttpRequest()
        self.request.GET['q'] = 'test'
        self.request.META = {
            'REQUEST_METHOD': 'GET',
            'HTTP_OPERATING_SYSTEM_VERSION': 'KIT KAT',
            'HTTP_PLATFORM': 'ANDROID',
            'HTTP_APP_VERSION': '1.0.0',
            'HTTP_USER_AGENT': 'AUTOMATED TEST',
            'HTTP_X_FORWARDED_FOR': '127.0.0.1',
        }
        self.request.path = '/'
        self.request.session = {}

    def test_process_request(self):
        response = self.middleware.process_request(self.request)
        self.assertIsNone(response)
        activity_log = self.request.activity_log
        self.assertEqual(activity_log.browser, 'Other')
        self.assertEqual(activity_log.os, 'Other')
        self.assertEqual(activity_log.device, 'Other')

    def test_without_x_forwarded(self):
        request = HttpRequest()
        request.GET['q'] = 'test'
        request.META = {
            'REQUEST_METHOD': 'GET',
            'HTTP_OPERATING_SYSTEM_VERSION': 'KIT KAT',
            'HTTP_PLATFORM': 'ANDROID',
            'HTTP_APP_VERSION': '1.0.0',
            'HTTP_USER_AGENT': 'AUTOMATED TEST',
            'REMOTE_ADDR': '172.18.0.1',
        }
        request.path = '/'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)

    def test_error(self):
        request = HttpRequest()
        request.GET['q'] = 'test'
        request.path = '/'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)

    def test_wo_search(self):
        request = HttpRequest()
        request.path = '/'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)

    def test_referer(self):
        request = HttpRequest()
        request.GET['q'] = 'test'
        request.META = {
            'REQUEST_METHOD': 'GET',
            'HTTP_OPERATING_SYSTEM_VERSION': 'KIT KAT',
            'HTTP_PLATFORM': 'ANDROID',
            'HTTP_APP_VERSION': '1.0.0',
            'HTTP_USER_AGENT': 'AUTOMATED TEST',
            'REMOTE_ADDR': '172.18.0.1',
            'HTTP_REFERER': 'http://127.0.0.1/commodity-codes/'
        }
        request.path = '/'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)

    def test_commodity_codes_referer(self):
        request = HttpRequest()
        request.GET['q'] = 'test'
        request.GET['catalog'] = 'psc'
        request.META = {
            'REQUEST_METHOD': 'GET',
            'HTTP_OPERATING_SYSTEM_VERSION': 'KIT KAT',
            'HTTP_PLATFORM': 'ANDROID',
            'HTTP_APP_VERSION': '1.0.0',
            'HTTP_USER_AGENT': 'AUTOMATED TEST',
            'REMOTE_ADDR': '172.18.0.1',
            'HTTP_REFERER': 'http://127.0.0.1/'
        }
        request.path = '/api/offerings/search/?q=test&catalog=psc'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)

    def test_contract_vehicles_referer(self):
        request = HttpRequest()
        request.GET['q'] = 'test'
        request.GET['catalog'] = 'gwac'
        request.META = {
            'REQUEST_METHOD': 'GET',
            'HTTP_OPERATING_SYSTEM_VERSION': 'KIT KAT',
            'HTTP_PLATFORM': 'ANDROID',
            'HTTP_APP_VERSION': '1.0.0',
            'HTTP_USER_AGENT': 'AUTOMATED TEST',
            'REMOTE_ADDR': '172.18.0.1',
            'HTTP_REFERER': 'http://127.0.0.1:8000/'
        }
        request.path = '/api/contractcodes/search/?q=test&catalog=gwac'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)

    def test_events_referer(self):
        request = HttpRequest()
        request.GET['q'] = 'test'
        request.META = {
            'REQUEST_METHOD': 'GET',
            'HTTP_OPERATING_SYSTEM_VERSION': 'KIT KAT',
            'HTTP_PLATFORM': 'ANDROID',
            'HTTP_APP_VERSION': '1.0.0',
            'HTTP_USER_AGENT': 'AUTOMATED TEST',
            'REMOTE_ADDR': '172.18.0.1',
            'HTTP_REFERER': 'http://127.0.0.1/events/'
        }
        request.path = '/'
        request.session = {}
        response = self.middleware.process_request(request)
        self.assertIsNone(response)
