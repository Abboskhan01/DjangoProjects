# Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Project
from files.views.attachment import AttachmentViewSet
from files.views.comment import CommentViewSet
from files.views.file import FileViewSet

router = DefaultRouter()
router.register('file', FileViewSet, 'file')
router.register('comments', CommentViewSet, 'comments')
router.register('attachments', AttachmentViewSet, 'attachments')

urlpatterns = [
    path('', include(router.urls)),
]
