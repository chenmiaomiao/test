from django.contrib import admin
from .models import submitted_tasks, tasks_available, task_total, task_factor

admin.site.register(submitted_tasks)
admin.site.register(tasks_available)
admin.site.register(task_total)
admin.site.register(task_factor)