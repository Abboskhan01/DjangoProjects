# Python
import datetime
import uuid

# Django
from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
from django.db import models

# Rest framework
from rest_framework.serializers import ValidationError

# Project
from shared.django.model import BaseModel

FILE_TYPES = {
    r'^(jpg|jpeg|png|gif|JPG)$': 'image'
}


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.datetime.today())[0:7]

    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            return 'file/%s/%s/%s.%s' % (
                folder, today, uuid.uuid4(), file_type)
        except Error:
            pass
    raise ValidationError(detail={'File type is unacceptable'})


class File(BaseModel):
    name = models.CharField(max_length=255, null=True)
    content_type = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to=upload_name)
