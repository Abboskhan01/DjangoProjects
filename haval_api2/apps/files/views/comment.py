from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from files.models import Comment
from files.serializers.comment import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.order_by('-id')
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'author', 'object_id', 'content_type']

    def get_queryset(self):
        query_set = super().get_queryset()
        if self.action == 'destroy':
            query_set = query_set
        else:
            query_set = query_set.filter(parent=None)
        return query_set
