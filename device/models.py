from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    added_on = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)