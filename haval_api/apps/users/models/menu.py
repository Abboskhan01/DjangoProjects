from django.contrib.auth.models import Permission
from django.db import models
from django.db.models import PROTECT


class MenuGroup(models.Model):
    name = models.JSONField()
    children = models.ManyToManyField('MenuPermissionsType')


class MenuPermissionsType(models.Model):
    title = models.JSONField()
    parent = models.ForeignKey('self', PROTECT, 'children')

    class Meta:
        ordering = ['-id']


class MenuPermissions(models.Model):
    title = models.JSONField()
    slug = models.CharField(max_length=255, unique=True)
    permission = models.OneToOneField(Permission, on_delete=PROTECT)
    icon = models.ForeignKey('files.File', PROTECT, 'menu_urls')

    class Meta:
        ordering = ['-id']
