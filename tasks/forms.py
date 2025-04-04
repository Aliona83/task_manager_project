from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Task

class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ['title','category','status','user','due_date','created_at','updated_at']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']