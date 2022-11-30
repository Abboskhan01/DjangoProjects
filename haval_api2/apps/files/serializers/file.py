# Django Rest Framework
from rest_framework import serializers

# Project
from files.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'name', 'file', 'content_type',)
