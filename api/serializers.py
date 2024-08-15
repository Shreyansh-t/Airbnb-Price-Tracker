from rest_framework import serializers
from properties.models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'desc', 'price']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['property', 'price']