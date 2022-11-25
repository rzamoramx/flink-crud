from rest_framework import serializers
from .models import Symbol


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('id', 'company_name', 'company_description', 'symbol', 'market_values')
