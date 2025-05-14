from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'status', 'category')
    list_filter = ('status', 'due_date', 'category')
    search_fields = ('title',)


