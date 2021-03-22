import logging

from rest_framework import serializers

activity_log = logging.getLogger('activity_log')


class ActivityLogSerializer(serializers.Serializer):
    action = serializers.CharField(max_length=255)
    feature = serializers.CharField(required=False, max_length=255, allow_blank=True)
    supplier = serializers.IntegerField(required=False)
    suppliers = serializers.ListField(required=False, child=serializers.IntegerField(), allow_empty=True)
    supplier_contacts = serializers.JSONField(required=False)
    log = serializers.JSONField(required=False)

    class Meta:
        fields = '__all__'
