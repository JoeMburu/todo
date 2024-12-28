from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def addTask(request):
    taskTitle = request.POST.get('title')
    Task.objects.create(title=taskTitle)
    return redirect('home')