from django.test import TestCase

from activitylogs.activity_log import ActivityLog
from activitylogs.constants import ActionTypes, DeviceTypes


class ActivityLogTests(TestCase):

    def setUp(self):
        self.log = ActivityLog(
            company_id=123,
            company_name='Test Company',
            ip='127.0.0.1',
            user_id=999,
            user_name='Name Lastname',
            user_type='Supplier',
        )

    def test_log(self):
        self.assertEqual(self.log.company_id, 123)
        self.assertEqual(self.log.company_name, 'Test Company')
        self.assertEqual(self.log.ip, '127.0.0.1')
        self.assertEqual(self.log.user_id, 999)
        self.assertEqual(self.log.user_name, 'Name Lastname')
        self.assertEqual(self.log.user_type, 'Supplier')

    def test_replace(self):
        self.log = self.log._replace_data(
            action=ActionTypes.MAIN_SEARCH,
            browser='Chrome',
            cc_id=123,
            company_id=123,
            company_name='New Company',
            cv_id=123,
            device_type=DeviceTypes.TABLET,
            device='Other',
            filter_name='',
            ip='172.0.0.1',
            items_num=1,
            items_type='type',
            num_of_suppliers=1,
            os_version='Other',
            os='Linux',
            search_catalog='psf',
            search_query='query',
            search_section='everywhere',
            section='general',
            subscription='Free',
            supplier_id=123,
            supplier_name='Supplier Name',
            supplier_section='General',
            user_id=123,
            user_name='New Name',
            user_request='Contact',
            user_type='Supplier',
            view_mode='mode',
        )
        self.assertEqual(self.log.action, ActionTypes.MAIN_SEARCH)
        self.assertEqual(self.log.browser, 'Chrome')
        self.assertEqual(self.log.cc_id, 123)
        self.assertEqual(self.log.company_id, 123)
        self.assertEqual(self.log.company_name, 'New Company')
        self.assertEqual(self.log.cv_id, 123)
        self.assertEqual(self.log.device_type, DeviceTypes.TABLET)
        self.assertEqual(self.log.device, 'Other')
        self.assertEqual(self.log.ip, '172.0.0.1')
        self.assertEqual(self.log.items_num, 1)
        self.assertEqual(self.log.items_type, 'type')
        self.assertEqual(self.log.num_of_suppliers, 1)
        self.assertEqual(self.log.os_version, 'Other')
        self.assertEqual(self.log.os, 'Linux')
        self.assertEqual(self.log.search_catalog, 'psf')
        self.assertEqual(self.log.search_query, 'query')
        self.assertEqual(self.log.search_section, 'everywhere')
        self.assertEqual(self.log.section, 'general')
        self.assertEqual(self.log.user_id, 123)
        self.assertEqual(self.log.user_name, 'New Name')
        self.assertEqual(self.log.user_type, 'Supplier')
        self.assertEqual(self.log.view_mode, 'mode')

    def test_to_dict(self):
        log_dict = self.log._to_dict()

        for k, v in log_dict.items():
            self.assertIsNotNone(v)
