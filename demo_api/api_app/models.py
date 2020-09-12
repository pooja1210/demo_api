from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache


# from .serializers import UserSerializer, CategorySerializer, DescriptionSerializer

# Create your models here.
class User(models.Model):
    user_id =    models.CharField(max_length=30)
    first_name =  models.CharField(max_length=254)
    last_name =  models.CharField(max_length=254)
    address =    models.CharField(max_length=254)
    City =  models.CharField(max_length=254)
    def __str__(self):
        return self.first_name

class Category(models.Model):
    title   = models.CharField(max_length=120) 
    def __str__(self):
        return self.title

class Description(models.Model):
    detail = models.CharField(max_length=120)
    category = models.ForeignKey(Category,related_name='description', on_delete= models.CASCADE)
    def __str__(self):
        return '%s: %s' %(self.category, self.detail)

def save_profile(sender, instance, **kwargs):
    from .views import cache_editor
    instance = cache.get("key11")
    cache_editor(instance)
    
post_save.connect(save_profile, sender=Category)

