from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category")

    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):
    STATUS_CHOICES = [
        ('Waiting', 'Waiting'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255, verbose_name="Title")
    due_date = models.DateTimeField(verbose_name="Due Date")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Waiting', verbose_name="Status")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date() and self.status != 'done'


