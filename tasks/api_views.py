from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status

from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer, TaskCreateUpdateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    # For Read-Only operations (GET requests)
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TaskSerializer
        # For Create/Update (POST, PUT, PATCH requests)
        return TaskCreateUpdateSerializer
class TaskFilterApiView(APIView):
    def get(self,request):
        status_param = request.GET.get('status')
        queryset = Task.objects.all()
        if status_param:
            queryset = queryset.filter(status=status_param)
        serializer = TaskSerializer(queryset,many=True)
        return Response(serializer.data)

