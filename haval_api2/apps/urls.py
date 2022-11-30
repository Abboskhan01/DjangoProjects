from django.urls import path, include

urlpatterns = [
    path('users/', include(('users.urls', 'users'), 'users')),
    path('files/', include(('files.urls', 'files'), 'files')),
    path('automobile/', include(('automobile.urls', 'automobile'), 'automobile')),
    path('calculator/', include(('calculator.urls', 'calculator'), 'calculator')),
]
