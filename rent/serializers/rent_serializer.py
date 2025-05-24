from rest_framework import serializers
from rent.models import Rent

class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'