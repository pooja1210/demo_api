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
        fields =["detail"] 
# class ProductSerializer(serializers.ModelSerializer):    
#     class Meta:        
#         model = Product       
#         fields =["title", "price"]    

class CategorySerializer(serializers.ModelSerializer):
    description = DescriptionSerializer(many=True)
    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('description')
        print("**&&",queryset)
        return queryset
    # product = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['title', "description"]
        def create(self, validated_data):
            description_data = validated_data.pop('description')
            category = Category.objects.create(**validated_data)
            for description_data in description_data:
                Description.objects.create(category=category, **description_data)
            return category





# class ProductSerializer(serializers.ModelSerializer):    
#     class Meta:        
#         model = Product      
#         fields = "__all__"  