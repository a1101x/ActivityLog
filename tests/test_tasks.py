from django.test import TestCase

from activitylogs.tasks import amplitude_event_send
from psf.models import SiteConfiguration


class AmplitudeEventSendTest(TestCase):

    def test_amplitude_send_event(self):
        site_conf = SiteConfiguration.get_solo()
        site_conf.amplitude = True
        site_conf.save()
        data = {'event_id': 'testid', 'user_id': 13}
        amplitude_event_send.delay(data)
