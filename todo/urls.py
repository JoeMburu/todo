
from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('completeTask/<int:task_id>/', views.completeTask, name='completeTask'),
    path('markTaskAsUndone/<int:task_id>/', views.markTaskAsUndone, name='markTaskAsUndone'),
    path('deleteTask/<int:task_id>/', views.deleteTask, name='deleteTask'),
    path('editTask/<int:task_id>/', views.editTask, name='editTask'),
    path('updateTask/<int:task_id>/', views.updateTask, name='updateTask'),
]
