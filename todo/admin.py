from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'updated_at')
    #list_filter = ('is_completed', 'created_at', 'updated_at')
    search_fields = ('title', )
    #ordering = ('-created_at',)

# Register your models here.
admin.site.register(Task, TaskAdmin)