from django.urls import path,include
from rest_framework import  routers

from api.views import CalculatorViewSet

router = routers.DefaultRouter()
router.register('calculator', CalculatorViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]