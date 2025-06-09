from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Task,User
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import requests
from django.http import JsonResponse
from newsapi import NewsApiClient



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
            messages.error(request, 'Password is wrong')
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
        tasks = tasks.filter(category=selected_category)

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
@login_required
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


from django.shortcuts import render, get_object_or_404, redirect

@login_required
def task_details(request, pk):
    category = Task.CATEGORY_CHOICES
    users = User.objects.all()
    task_status = Task.STATUS_CHOICES
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.category = request.POST.get('category')
        # add more fields as needed
        task.save()
        return redirect('task_list')  # or redirect to the same detail page

    return render(request, 'tasks/task_details.html', {
        'task': task,
        'category': category,
        'users': users,
        'task_status': task_status,
    })


def weather_view(request):
    # List of cities for the dropdown
    cities = ['London', 'New York', 'Tokyo', 'Paris', 'Nairobi', 'Sydney', 'Cairo','Ireland']
    city = 'London'

    if request.method == 'POST':
        city = request.POST.get('city', 'London')

    api_key = "4a1fd4150fd249368e793057252605"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&aqi=no&alerts=no"

    response = requests.get(url)
    data = response.json()

    weather_data = None
    if response.status_code == 200 and 'forecast' in data:
        current = data['current']
        forecast_days = data['forecast']['forecastday']

        weather_data = {
            'city': data['location']['name'],
            'description': current['condition']['text'],
            'temperature': current['temp_c'],
            'icon': 'https:' + current['condition']['icon'],
            'forecast': [
                {
                    'date': day['date'],
                    'temp': day['day']['avgtemp_c'],
                    'icon': 'https:' + day['day']['condition']['icon'],
                    'text': day['day']['condition']['text']
                } for day in forecast_days
            ]
        }

    return render(request, 'tasks/weather.html', {
        'weather': weather_data,
        'cities': cities,
        'selected_city': city
    })



def autocomplete_city(request):
    query = request.GET.get('q')
    api_key = "4a1fd4150fd249368e793057252605"

    if not query:
        return JsonResponse([], safe=False)

    url = f"http://api.weatherapi.com/v1/search.json?key={api_key}&q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse([], safe=False)

def news_view(request):
    api_key = "07b57b16fd014b3b8a9c1b1937be4300"
    newsapi = NewsApiClient(api_key=api_key)

    # Fetch top headlines
    top_headlines = newsapi.get_top_headlines(
        q='technology',
        language='en',
        country='us'
    )

    articles = top_headlines['articles']

    context = {
        'articles': articles
    }

    return render(request, 'news.html', context)

