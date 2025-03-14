from rest_framework import serializers

from api.models import Calculator


class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        fields = ["expression"]
        ordering = ["-expression"]