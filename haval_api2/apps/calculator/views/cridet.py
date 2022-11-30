# DRF
from rest_framework import  viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Projects
from calculator.models import Cridet
from calculator.serializers import CridetModelSezializer


class CridetViewSet(viewsets.ModelViewSet):
    queryset = Cridet.objects.order_by('id')
    serializer_class = CridetModelSezializer