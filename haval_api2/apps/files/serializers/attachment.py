# Django Rest Framework
from rest_framework import serializers

# Project
from files.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = [
            'id',
            'author',
            'object_id',
            'content_type',
            'file',
        ]
        extra_kwargs = {
            'object_id': {"write_only": True},
            'content_type': {"write_only": True},
        }
