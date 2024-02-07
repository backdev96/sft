from rest_framework import serializers

from .models import Contract, Manufacturer


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = (
            "id",
            "name",
            "manufacturers"
        )
    
    manufacturers = serializers.SerializerMethodField()

    def get_manufacturers(self, obj: Contract):
        return Manufacturer.objects.filter(
            products__application__contract=obj
        ).distinct().values_list('id', flat=True)
