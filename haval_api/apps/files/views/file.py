# Django
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import MultiPartParser

# Create your views here.
from files.models import File
from files.serializers.file import FileSerializer


class FileViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  GenericViewSet):
    queryset = File.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser]
