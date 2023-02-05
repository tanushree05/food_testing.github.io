from rest_framework import serializers
from .models import FoodData, FoodItem

class FoodDataSerializer(serializers.ModelSerializer):

    class Meta:
        model= FoodItem
        fields = '__all__'
        depth = 2 


