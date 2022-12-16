from django.shortcuts import render
from ecommerce.inventory.models import Category, Product
from ecommerce.drf.serializer import CategorySerializer,ProductSerializer
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
     
    
    
    