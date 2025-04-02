from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import task_list,delete_task

urlpatterns = [
    path('', task_list, name='task-list'),
    path('tasks/delete_task/<int:pk>/', delete_task, name='delete_task'),

]