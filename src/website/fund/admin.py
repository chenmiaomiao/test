from django.contrib import admin
from .models import task_list, task_factor

admin.site.register(task_list)
admin.site.register(task_factor)