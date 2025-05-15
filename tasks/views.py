from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Task,User
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, 'Неправильный логин или пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    category = Task.CATEGORY_CHOICES
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
        'category': category,
        'task_status': task_status,
        'selected_category': selected_category,
        'selected_status': selected_status,
    }

    return render(request, 'tasks/tasks.html', context)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

def add_task(request):

    users = User.objects.all()
    task_status = Task.STATUS_CHOICES
    category = Task.CATEGORY_CHOICES
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        category = Task.CATEGORY_CHOICES
        users = User.objects.all()
        task_status = Task.STATUS_CHOICES
    return render(request, 'tasks/add_task.html', {'form': form,  'category': category,
        'users': users,
        'task_status': task_status,})

def task_details(request, pk):
    category = Task.CATEGORY_CHOICES
    users = User.objects.all()
    task_status = Task.STATUS_CHOICES
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_details.html', {'task': task, 'category': category,
        'users': users,
        'task_status': task_status,})

