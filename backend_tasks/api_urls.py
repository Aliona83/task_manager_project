from django.urls import path
from . import api_views

urlpatterns = [
    path('tasks/', api_views.api_task_list),
    path('tasks/add/', api_views.api_add_task),
    path('tasks/<int:pk>/', api_views.api_task_details),
    path('tasks/<int:pk>/delete/', api_views.api_delete_task),
    path('weather/', api_views.api_weather),
]

