from rest_framework import viewsets 
from .serializers import UserSerializer, CategorySerializer, DescriptionSerializer
from .models import User, Category, Description

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ModelViewSet


class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    # start = time.time()
    # end =time.time()
    # print("time take", end-start)   
class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all() 
    queryset = CategorySerializer.setup_eager_loading(queryset)
    serializer_class = CategorySerializer
    
class DescriptionViewSet(viewsets.ModelViewSet): 
    queryset = Description.objects.all() 
    serializer_class = DescriptionSerializer


    
# class ProductViewSet(viewsets.ModelViewSet): 
#     queryset = User.objects.all() 
#     serializer_class = ProductSerializer