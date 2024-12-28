from django.shortcuts import render
from todo.models import Task

def home(request):
    completed_tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    uncompleted_tasks = Task.objects.filter(is_completed=True)

    return render(request, 'home.html', {'completed_tasks': completed_tasks, 'uncompleted_tasks': uncompleted_tasks})