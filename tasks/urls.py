from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import TaskList

urlpatterns = [
    path('tasks/',TaskList.as_view(),name='task-list')
]