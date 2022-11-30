from django.contrib.auth.models import GroupManager
from django.db import models
from django.db.models import CASCADE


class CustomGroup(models.Model):
    title = models.JSONField(unique=True)
    permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='custom_group_permissions')

    objects = GroupManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)

    def natural_key(self):
        return str(self.id)


class Role(models.Model):
    name = models.JSONField(default=dict, null=True, blank=True)
    groups = models.ManyToManyField('CustomGroup', related_name='roles')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)


class UserRole(models.Model):
    user = models.ForeignKey('users.User', CASCADE)
    role = models.ForeignKey('users.Role', CASCADE)

    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
