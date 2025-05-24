from rest_framework import serializers
from frontend_tasks.models import Task
from django.contrib.auth.models import User

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # To show username instead of user ID

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status', 'category', 'user', 'created_at', 'updated_at']

# Task Creation/Update Serializer (for POST, PUT, PATCH requests)
class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'category', 'user']
