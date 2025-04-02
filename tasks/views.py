from django.shortcuts import render
from .models import Task,Category


def task_list(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    task_status = Task.STATUS_CHOICES

    # Filtering logic
    selected_category = request.GET.get('category')
    selected_status = request.GET.get('status')

    if selected_category:
        tasks = tasks.filter(category_id=selected_category)

    if selected_status:
        tasks = tasks.filter(status=selected_status)

    context = {
        'tasks': tasks,
        'categories': categories,
        'task_status': task_status,
        'selected_category': selected_category,
        'selected_status': selected_status,
    }

    return render(request, 'tasks/tasks.html', context)

def delete_task(request,pk):
    pass