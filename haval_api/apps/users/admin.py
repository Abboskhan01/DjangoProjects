from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from users.models import User


@admin.register(User)
class Admin(UserAdmin):
    fieldsets = (
        (None,
         {'fields': (
             'username', 'password', 'theme')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
