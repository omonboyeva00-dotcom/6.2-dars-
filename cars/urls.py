from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarModelViewSet

router = DefaultRouter()
router.register(r'cars', CarModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
