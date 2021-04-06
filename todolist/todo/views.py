from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import TodoList
from todo.forms import TodoForm
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
# Add Task API
def addTodo(request):
    if request.method == "POST":
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        messages.success(request,('New Task Added!'))
        return redirect('addTodo')
    else:
        form = TodoForm()
        all_tasks = TodoList.objects.all()
        # define paginator on object all_tasks 
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        # Gets page with page no in page and retrieves all contents in that page.
        all_tasks = paginator.get_page(page)
        
        return render(request,'todo.html',{'all_tasks':all_tasks,'form':form,'now1':datetime.now()})

def edit_task(request,task_id):
    if request.method == "POST":
        task = TodoList.objects.get(pk=task_id)
        form = TodoForm(request.POST or None,instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited!"))
        return redirect('addTodo')
    else:
        form = TodoForm()
        # for checking status of task
        task_obj = TodoList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj,'form':form})
def delete_task(request,task_id):
    task = TodoList.objects.get(id=task_id)
    task.delete()

    return redirect("addTodo")