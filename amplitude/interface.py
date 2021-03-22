import json
import requests

from django.conf import settings


API_SETTINGS = {
    'api_key': settings.AMPLITUDE_API_KEY,
    'api_url': settings.AMPLITUDE_API_URL,
}


class AmplitudeApi:

    def send_event(self, event):
        '''
        Send amplitude event.
        '''
        if all((API_SETTINGS['api_url'], API_SETTINGS['api_key'])):
            headers = {
                'Content-Type': 'application/json',
                'Accept': '*/*',
            }
            data = {
                'api_key': API_SETTINGS['api_key'],
                'options': {'min_id_length': 1},
                'events': [event],
            }
            response = requests.post(
                API_SETTINGS['api_url'],
                data=json.dumps(data),
                headers=headers,
            )
            return response
        else:
            return 'API KEY or API URL do not set.'


amplitude_event = AmplitudeApi()
