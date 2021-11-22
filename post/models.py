from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    car_name = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    description = models.TextField()
    seller = models.ForeignKey(get_user_model() ,on_delete=CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.car_name
