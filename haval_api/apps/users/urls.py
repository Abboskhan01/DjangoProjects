# Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# Project
from users.views.auth import AuthViewSet, LoginView
from users.views.role import RoleViewSet, GroupViewSet, PermissionViewSet
from users.views.user import UserViewSet

router = DefaultRouter()
router.register('auth', AuthViewSet, 'auth')
router.register('users', UserViewSet, 'users')
router.register('roles', RoleViewSet, 'roles')
router.register('groups', GroupViewSet, 'groups')
router.register('permissions', PermissionViewSet, 'permissions')

urlpatterns = [
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', LoginView.as_view(), name='login'),
    path('', include(router.urls)),

]
