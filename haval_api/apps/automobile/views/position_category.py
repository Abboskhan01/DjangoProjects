from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from automobile.models import PositionCategory
from automobile.serializers import PositionCategorySerializer


class PositionCategoryViewSet(viewsets.ModelViewSet):
    queryset = PositionCategory.objects.order_by('id')
    serializer_class = PositionCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = "__all__"
    search_field = "__all__"
