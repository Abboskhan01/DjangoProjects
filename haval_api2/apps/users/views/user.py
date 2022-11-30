from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers.user import UserModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    ordering = ['-date_joined']
    search_fields = ['username']
