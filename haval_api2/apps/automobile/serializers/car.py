from rest_framework import serializers

from automobile.models import Car


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

