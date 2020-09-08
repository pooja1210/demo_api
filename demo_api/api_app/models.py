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