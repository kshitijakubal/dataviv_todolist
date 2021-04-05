from django.contrib import admin
from todo.models import TodoList

# Register your models here.
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['id','task','task_image','priority']