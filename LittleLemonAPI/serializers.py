from django.contrib.auth.models import User
from rest_framework import serializers

from LittleLemonAPI import models


class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'user_permissions')
