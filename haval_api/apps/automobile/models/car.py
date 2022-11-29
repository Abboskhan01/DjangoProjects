from django.db import models
from shared.django.model import BaseModel
from colorfield.fields import ColorField


class Car(BaseModel):
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red")
    ]
    title = models.CharField(max_length=255)
    cost_from = models.FloatField()
    color = ColorField(choices=COLOR_CHOICES)
    about = models.TextField()
    internal_possibility = models.TextField()
    appearance = models.TextField()

    internal_photo = models.ImageField()
    external_photo = models.ImageField()
    side_photo = models.ImageField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)


