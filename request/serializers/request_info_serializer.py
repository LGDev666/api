from rest_framework import serializers
from request.models import RequestInfo

class RequestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestInfo
        fields = '__all__'