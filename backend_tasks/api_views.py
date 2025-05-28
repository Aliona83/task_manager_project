from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from frontend_tasks.models import Task
from .serializers import TaskSerializer, TaskCreateUpdateSerializer
from django.shortcuts import get_object_or_404
import requests


# Returns a JSON list of tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_task_list(request):
    tasks = Task.objects.filter(user=request.user)

    category = request.GET.get('category')
    status = request.GET.get('status')

    if category:
        tasks = tasks.filter(category=category)
    if status:
        tasks = tasks.filter(status=status)

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# Creates a new task for the authenticated user.
# Accepts POST data, validates it, and returns the created task in JSON format.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_task(request):
    serializer = TaskCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.save(user=request.user)
        return Response(TaskSerializer(task).data, status=201)
    return Response(serializer.errors, status=400)

# Deletes a task owned by the authenticated user.
# Only accessible via DELETE request with the task's primary key.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return Response({"detail": "Task deleted"})

# Retrieves or updates a specific task owned by the authenticated user.
# GET returns task details; PUT updates the task with provided data.
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def api_task_details(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskCreateUpdateSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(TaskSerializer(task).data)
        return Response(serializer.errors, status=400)


# Fetches 3-day weather forecast for a given city from WeatherAPI.
# Returns weather data in JSON format. Defaults to 'London' if no city is provided.
@api_view(['GET'])
def api_weather(request):
    city = request.GET.get('city', 'London')
    api_key = "your_actual_key"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&aqi=no&alerts=no"

    response = requests.get(url)
    if response.status_code != 200:
        return Response({"error": "Could not fetch weather data"}, status=400)

    data = response.json()
    return Response(data)




