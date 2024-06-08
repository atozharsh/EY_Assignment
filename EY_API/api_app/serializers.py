from django.contrib.auth.models import Group, User
from rest_framework import serializers


class AddNumbersSerializer(serializers.Serializer):
    batchid = serializers.CharField(max_length=100)
    # payload = serializers.ListField(child=serializers.ListField(child=serializers.IntegerField()))
    payload = serializers.ListField()

class ResponseDataSerializer(serializers.Serializer):
    batchid = serializers.CharField(max_length=100)
    response = serializers.ListField()
    status = serializers.CharField(max_length=100)
    started_at = serializers.DateTimeField()
    completed_at = serializers.DateTimeField()

