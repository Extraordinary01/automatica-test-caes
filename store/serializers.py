from rest_framework import serializers
from .models import *

class TradingPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradingPoint
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = '__all__'

