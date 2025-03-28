from rest_framework import serializers
from .models import Category, Task
from django.contrib.auth.models import User

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested category serializer
    user = serializers.StringRelatedField()  # To show username instead of user ID

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'category', 'user', 'created_at', 'updated_at']

# Task Creation/Update Serializer (for POST, PUT, PATCH requests)
class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'category', 'user']
