import json

from logstash_async.transport import TcpTransport


class ActivityLogTransport(TcpTransport):

    def _send_via_socket(self, data):
        dict_data = json.loads(data)
        # HeadlessChrome is a browser name used by rendertron
        # we do not need to store logs from rendertron
        browser = dict_data.get('browser', None)

        if browser != 'HeadlessChrome':
            data_to_send = self._convert_data_to_send(data)
            self._sock.sendall(data_to_send)

        action = dict_data.get('action', None)
        browser = dict_data.get('browser', None)
        device_id = dict_data.get('deviceId', None)
        device_type = dict_data.get('deviceType', None)

        if all((action, device_id, device_type != 'Bot', browser != 'HeadlessChrome')):
            from activitylogs.tasks import amplitude_event_send
            amplitude_event_send.delay(dict_data)
