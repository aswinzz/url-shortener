from rest_framework import serializers

class URLSerializer(serializers.Serializer):
    short=serializers.CharField()
    url=serializers.CharField()
    clicks=serializers.IntegerField()
    created=serializers.DateTimeField()