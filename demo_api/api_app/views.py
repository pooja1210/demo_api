from rest_framework import viewsets 
from .serializers import UserSerializer, CategorySerializer, DescriptionSerializer
from .models import User, Category, Description
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from  django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ViewSet):
     def list(self, request):
        queryset = Category.objects.all()
        queryset = CategorySerializer.setup_eager_loading(queryset)
        post_data = CategorySerializer(queryset, many=True).data
        cache.set('key11', post_data, 60 * 15)
        return Response(post_data)

class DescriptionViewSet(viewsets.ModelViewSet): 
    queryset = Description.objects.all() 
    serializer_class = DescriptionSerializer
def cache_editor(instance,*args, **kwargs):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    cache.set('key11', serializer.data, 60 * 15)

    