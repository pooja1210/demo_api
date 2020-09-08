from rest_framework import serializers 
from typing import Dict, Any
from .models import User  
class UserSerializer(serializers.ModelSerializer):  
    class Meta: 
        model = User 
        fields = ('user_id', 'first_name', 'last_name', 'address', 'City') 
        read_only_fields = fields
