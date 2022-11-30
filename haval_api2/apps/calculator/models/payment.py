from django.db import models
from shared.django.model import BaseModel


class Payment(models.Model):
    credit = models.ForeignKey('calculator.Cridet', on_delete=models.CASCADE, related_name='payments')
    order = models.IntegerField(default=1)
    sum = models.FloatField(default=0)
    percent = models.FloatField(default=12)
    total = models.FloatField(default=0)
    remain = models.FloatField(default=0)

    def __str__(self):
        return str(self.order)
