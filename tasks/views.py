from django.shortcuts import render
from .models import Task,Category


def task_list(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    task_status = Task.STATUS_CHOICES
    context = {'tasks':tasks,'categories':categories,'task_status':task_status}
    return render(request,'tasks/tasks.html',context)

def delete_task(request,pk):
    pass