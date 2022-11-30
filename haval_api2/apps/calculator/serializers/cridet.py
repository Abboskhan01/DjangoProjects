from rest_framework import serializers

# Project
from calculator.models import Cridet


class CridetModelSezializer(serializers.ModelSerializer):
    class Meta:
        model = Cridet
        fields = "__all__"
