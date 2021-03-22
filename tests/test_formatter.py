import logging
from datetime import datetime

from django.test import TestCase
from testfixtures import LogCapture

from activitylogs.activity_log import ActivityLog
from activitylogs.formatter import ActivityLogFormatter


class ActivityLogFormatterTestCase(TestCase):

    def setUp(self):
        self.logger = logging.getLogger('activity_log')
        self.log = ActivityLog(
            user_id=999,
            user_type='Supplier',
            ip='127.0.0.1',
        )

    def test_logging(self):
        with LogCapture() as l:
            self.logger.info('registration', extra={**self.log._to_dict()})
            l.check(
                ('activity_log', 'INFO', 'registration'),
            )

    def test_replace(self):
        with LogCapture() as l:
            self.logger.info('replace_data', extra={**self.log._to_dict(user_id=1999)})
            l.check(
                ('activity_log', 'INFO', 'replace_data'),
            )

    def test_tags(self):
        with LogCapture() as l:
            self.logger.info('extra', extra={'tags': 'search', **self.log._to_dict()})
            l.check(
                ('activity_log', 'INFO', 'extra'),
            )

    def test_formatter(self):
        formatter = ActivityLogFormatter()
        record = logging.LogRecord(name='test', level='INFO', pathname='/test', lineno=1, msg='test', args=(), exc_info=None)
        self.assertIsNotNone(formatter.format(record))
