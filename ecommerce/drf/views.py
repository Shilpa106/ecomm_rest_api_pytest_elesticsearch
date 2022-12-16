from django.shortcuts import render
from ecommerce.inventory.models import (
    Category,
    Product,
    ProductInventory
)
from ecommerce.drf.serializer import (
    CategorySerializer,
    ProductSerializer,
    ProductInventorySerializer,
)

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class CategoryList(APIView):
    """
    Return list of all categories
    """
    
    def get(self,request):
        queryset=Category.objects.all()
        serializer=CategorySerializer(queryset,many=True)
        return Response(serializer.data) 
    
class ProductByCategory(APIView):
    """
    Return product by category
    """
    def get(self, request,query=None):
        queryset=Product.objects.filter(category__slug=query)
        serializer=ProductSerializer(queryset, many=True)
        return Response(serializer.data)
     
    
    
class ProductInventoryByWebId(APIView):
    """
    Return Sub Product by WebId 
    """
    
    def get(self,request, query=None):
        queryset = ProductInventory.objects.filter(product__web_id=query)
        serializer=ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)
        pass 