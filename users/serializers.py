from rest_framework import serializers
from .models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = User