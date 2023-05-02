
from rest_framework import serializers
from recordapp.models import SaleItem

class SaleItemserializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields=(
            'date', 'amount','item_id','user_id'
        )