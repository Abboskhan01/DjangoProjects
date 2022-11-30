# DRF
from rest_framework import  viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Projects
from calculator.models import Payment, Cridet
from calculator.serializers import PaymentModelSezializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.order_by('id')
    serializer_class = PaymentModelSezializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['credit']
