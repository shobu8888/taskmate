from django.shortcuts import render , redirect
from django.http import *
from .models import TaskList
from todolist.forms import TaskFrom
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskFrom(request.POST or None)
        if form.is_valid():
            form.save(commit = False).manage = request.user
            form.save()
            messages.success(request,("New Task Added"))
        return redirect('todolist')
    else:
        all_task = TaskList.objects.filter(manage = request.user)
        paginator = Paginator(all_task,5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request,'todolist.html' , {'all_task':all_task})

@login_required
def delete_task(request, task_id):
        task = TaskList.objects.get(pk=task_id)
        if task.manage == request.user:
            task.delete()
        else:
            messages.success(request,("Access Restricted"))
        return redirect('todolist')

@login_required
def complete_task(request, task_id):
        task = TaskList.objects.get(pk=task_id)
        if task.manage == request.user:
            task.done = True
            task.save()
        else:
            messages.success(request,("Access Restricted"))
        return redirect('todolist')
@login_required
def pending_task(request, task_id):
        task = TaskList.objects.get(pk=task_id)
        task.done = False
        task.save()
        return redirect('todolist')
@login_required
def edit_task(request,task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskFrom(request.POST or None , instance = task)
        if form.is_valid():
            form.save()
            messages.success(request,("Task has been updated"))
        return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request,'edit.html' , {'task':task})

def index(request):
    welcome_text = 'Welcome !! to Index Us'
    return render(request,'index.html' )

def aboutus(request):
    welcome_text = 'Welcome !! to About Us'
    return render(request,'aboutus.html' , {'welcome_text':welcome_text})

def contactus(request):
    welcome_text = 'Welcome !! to Contact Us'
    return render(request,'contactus.html' , {'welcome_text':welcome_text})
