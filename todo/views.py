from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def addTask(request):
    taskTitle = request.POST.get('title')
    Task.objects.create(title=taskTitle)
    return redirect('home')

def completeTask(request, task_id):
    task = Task.objects.get(id=task_id) # get_object or 404()
    task.is_completed = True
    task.save()
    return redirect('home')

def deleteTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')


def markTaskAsUndone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')
    
def editTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'edit_task.html', {'task_id': task.id, 'task_title': task.title})

def updateTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.title = request.POST.get('title')    
    task.save()
    return redirect('home')