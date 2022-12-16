
from ecommerce.inventory.models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name','slug','is_active']
        read_only=True

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=['name','web_id']
        read_only=True
        editable=False 
        