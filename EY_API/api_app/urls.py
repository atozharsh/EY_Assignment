from rest_framework import routers
from django.urls import include, path

from .views import *

router = routers.DefaultRouter()
router.register(r'add', AddNumbersViewSet, basename='add_numbers')

urlpatterns = [
    path('', include(router.urls)),
]