from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

# Project
from automobile.models import Car, PositionCategory
from automobile.serializers import CarModelSerializer, ComparePositionSerializer
from automobile.filters.car import CarFilter


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.order_by('id')
    serializer_class = CarModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['title', 'color', 'cost_from', 'is_active']
    filter_class = CarFilter
    filterset_fields = ['color', 'cost_from']

    @action(['GET'], detail=True, serializer_class=ComparePositionSerializer)
    def compare(self, request, pk=None):
        compared = PositionCategory.objects.filter(car_id=pk)
        serializer = self.serializer_class(compared, many=True)
        return Response(serializer.data)
