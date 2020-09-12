from rest_framework import serializers 
from typing import Dict, Any
from .models import User,  Category, Description
import cProfile
class UserSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta: 
        model = User 
        fields = ('user_id', 'first_name', 'last_name', 'address', 'City') 

class DescriptionSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Description       
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):
    description = DescriptionSerializer(read_only=True, many=True)
    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('description')
        return queryset
    class Meta:
        model = Category
        fields =  ["title",  "description"]
    