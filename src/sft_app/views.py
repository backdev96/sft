from django.shortcuts import render

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


from .models import Contract
from .serializers import ContractSerializer

# Create your views here.
class ContractViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Contract.objects.prefetch_related("applications__products")
    serializer_class = ContractSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
