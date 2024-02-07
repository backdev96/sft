from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ContractViewSet


router = DefaultRouter()
router.register("contracts", ContractViewSet, basename="contracts")

urlpatterns = [
    path("", include(router.urls))
]
