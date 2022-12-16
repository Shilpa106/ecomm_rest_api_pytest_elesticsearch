
from django.contrib import admin
from django.urls import path

from ecommerce.drf.views import CategoryList, ProductByCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inventory/category/all/',CategoryList.as_view()),
    path('api/inventory/products/category/<str:query>/',ProductByCategory.as_view()),
    
]
