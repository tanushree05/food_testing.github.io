from django.db import models

from rest_framework_api_key.models import APIKey
api_key, key = APIKey.objects.create_key(name="my-remote-service")
# Create your models here.
class FoodData (models.Model):
    # ph_value = models.DecimalField()
    humidity = models.DecimalField(max_digits=5,null=True, decimal_places=2)
    methane = models.DecimalField(max_digits=5,null=True, decimal_places=2)
    temperature = models.DecimalField(max_digits=5,null=True, decimal_places=2)

class FoodItem(models.Model):
    item = models.CharField(max_length=15)
    data = models.ForeignKey(FoodData,on_delete=models.CASCADE, null=True)

