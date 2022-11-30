# Django
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from files.models import Attachment
from files.serializers.attachment import AttachmentSerializer


class AttachmentViewSet(ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
