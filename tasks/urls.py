from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import task_list,delete_task,register_view,login_view,logout_view

urlpatterns = [
path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', task_list, name='task_list'),
    path('tasks/delete_task/<int:pk>/', delete_task, name='delete_task'),

]