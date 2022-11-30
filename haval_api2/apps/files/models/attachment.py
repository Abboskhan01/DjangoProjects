import os
from django.db.models import CASCADE, Model, PositiveIntegerField, FileField, ForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def get_upload_path(instance, filename):
    return os.path.join(f'{instance.content_type.model}', f'{instance.object_id}', filename)


class Attachment(Model):
    # Relationships
    author = ForeignKey('users.User', CASCADE, 'attachments')
    content_type = ForeignKey(ContentType, CASCADE, 'attachments')
    content_object = GenericForeignKey('content_type', 'object_id', )

    # Fields
    object_id = PositiveIntegerField()
    # object_id = PositiveIntegerField()
    file = FileField(upload_to=get_upload_path)

    def __str__(self):
        return str(self.id)
