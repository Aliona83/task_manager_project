from rest_framework import serializers
from frontend_tasks.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'status', 'category', 'user', 'created_at', 'updated_at']


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'status', 'category', 'user']
