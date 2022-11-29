from django.urls import path, include
from rest_framework.routers import DefaultRouter


from automobile.views import CarViewSet , PositionCategoryViewSet

router = DefaultRouter()

router.register('car', CarViewSet, 'car')
router.register('position-category', PositionCategoryViewSet, 'position-category')

urlpatterns = [
    path('', include(router.urls))
]