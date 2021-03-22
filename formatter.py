from logstash_async.formatter import DjangoLogstashFormatter

from activitylogs.constants import FEATURE_TYPES


class ActivityLogFormatter(DjangoLogstashFormatter):

    def get_feature_type(self, message):
        return FEATURE_TYPES.get(message, None)

    def format(self, record):
        message = self._get_record_fields(record)
        message.update({
            '@timestamp': self._format_timestamp(record.created),
            '@version': '1',
            'host': self._host,
            'level': record.levelname,
            'logsource': self._logsource,
            'feature': self.get_feature_type(record.getMessage()),
            'pid': record.process,
            'program': self._program_name,
            'type': self._message_type,
        })
        extra_fields = self._get_extra_fields(record)
        message.update(extra_fields)
        return self._serialize(message)
