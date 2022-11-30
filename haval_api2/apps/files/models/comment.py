from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import ForeignKey, CASCADE, TextField, PositiveIntegerField

from shared.django.model import BaseModel


class Comment(BaseModel):
    # Relationships
    parent = ForeignKey('self', CASCADE, 'children', null=True, default=None, blank=True)
    author = ForeignKey('users.User', CASCADE, 'comments')
    content_type = ForeignKey(ContentType, CASCADE, 'comments')
    content_object = GenericForeignKey('content_type', 'object_id')

    # Fields
    object_id = PositiveIntegerField()
    message = TextField()

    def __str__(self):
        return str(self.id)
