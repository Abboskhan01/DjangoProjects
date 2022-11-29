from django.db import models
from shared.django.model import BaseModel
from django.db.models import Min

# Project
from automobile.models import Car


class PositionCategory(BaseModel):
    # relations
    car = models.ForeignKey('automobile.Car', on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    engine = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    available_volume = models.CharField(max_length=255)
    drive_type = models.CharField(max_length=255)
    transmission_box = models.CharField(max_length=255)
    overclocking_time = models.FloatField()
    max_speed = models.IntegerField()

    # security
    lockingRearWheelDifferential = models.BooleanField(default=False)
    automaticAutoHold = models.BooleanField(default=False)
    childSeatLock = models.BooleanField(default=False)

    # exterior
    led_headlight = models.CharField(max_length=255)
    full_weight = models.FloatField()
    empty_weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    seats_count = models.IntegerField()

    def __str__(self):
        return str(self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.cost and self.car:
            min_cost = PositionCategory.objects.aggregate(Min('cost'))['cost__min']
            if min_cost is None:
                min_cost = 0
            if self.cost < min_cost:
                min_cost = self.cost
            car = Car.objects.get(id=self.car.id)
            car.cost_from = min_cost
            car.save()
        super().save(force_insert, force_update, using, update_fields)
