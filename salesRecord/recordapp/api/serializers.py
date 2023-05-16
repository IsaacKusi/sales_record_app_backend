
from rest_framework import serializers
from recordapp.models import SaleItem

class SaleItemserializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields=(
            '__all__'
        )