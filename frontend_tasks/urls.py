from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .views import task_list,delete_task,register_view,login_view,logout_view,task_details,add_task,weather_view,autocomplete_city

urlpatterns = [
path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', task_list, name='task_list'),
    path('frontend_tasks/delete_task/<int:pk>/', delete_task, name='delete_task'),
    path('task_details/<int:pk>/', task_details, name='task_details'),
    path('add_task/', add_task, name='add_task'),
    path('weather/', weather_view, name='weather'),
    path('autocomplete/', autocomplete_city, name='autocomplete_city'),




]