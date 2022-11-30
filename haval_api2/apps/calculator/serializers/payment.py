from rest_framework import serializers

# Project
from calculator.models import Payment, Cridet
from automobile.models import PositionCategory, Car


class PaymentModelSezializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        