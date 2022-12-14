from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import SET_NULL

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class User(AbstractUser):
    LANGUAGES_CHOICES = (
        ('uz', 'Lotin'),
        ('oz', 'Uzbek'),
        ('ru', 'Russian'),
    )

    THEMES_CHOICES = (
        ('0', 'Dark'),
        ('1', 'Light'),
    )

    language = models.CharField(max_length=25, choices=LANGUAGES_CHOICES, blank=True, null=True)
    photo = models.ForeignKey('files.File', SET_NULL, null=True)
    theme = models.CharField(max_length=24, choices=THEMES_CHOICES, default=THEMES_CHOICES[1], blank=True, null=True)
    phone_number = models.CharField(max_length=13, validators=[phone_regex], blank=True, null=True, default=None)
    mac_address = models.JSONField(default=dict, null=True, blank=True)
    role = models.ManyToManyField("users.Role", through='users.UserRole')

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        ordering = ['-id']
