import json

from celery import shared_task

from activitylogs.amplitude.interface import amplitude_event
from activitylogs.amplitude.properties import amplitude_properties
from psf.models import SiteConfiguration


@shared_task
def amplitude_event_send(data):
    if SiteConfiguration.get_solo().amplitude:
        properties = amplitude_properties.to_dict(data)
        amplitude_event.send_event(properties)
