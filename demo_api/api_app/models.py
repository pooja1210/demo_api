from django.db import models

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

# class Product(models.Model):
#     title       = models.CharField(max_length=120) 
#     category    = models.ForeignKey(Category,related_name='description',on_delete=models.CASCADE)
#     price = models.DecimalField(decimal_places=2, max_digits=10000)
#     def __str__(self):
#         return self.title
    

