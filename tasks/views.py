from django.shortcuts import render
from .models import Task
from rest_framework.views import APIView
from .serializers import TaskSerializer
from rest_framework.response import Response
from . import views

class TaskList(APIView):
    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
