from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from files.models import Comment
from users.serializers.user import UserClientSerializer


class CommentSerializer(serializers.ModelSerializer):
    parent = PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = '__all__'

        read_only_fields = ['created_date', 'modified_date']
        extra_kwargs = {
            'object_id': {"write_only": True},
            'content_type': {"write_only": True},
            'parent': {"required": False},
        }

    def to_representation(self, instance):
        to_representation = super().to_representation(instance)
        if instance.children:
            to_representation['children'] = CommentSerializer(instance.children.all(), many=True).data
        to_representation['author'] = UserClientSerializer(instance.author).data
        return to_representation
