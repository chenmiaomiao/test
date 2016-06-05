from django.shortcuts import render
from .forms import SubmittedTasksForm
from .models import submitted_tasks, tasks_available, task_total, task_factor

# Create your views here.

def index(request):
    submitted_tasks_items = submitted_tasks.objects.all()
    tasks_available_items = tasks_available.objects.all()
    task_total_items = task_total.objects.all()
    task_factor_items = task_factor.objects.all()
    
    return render(request, 'fund/index.html', {'submitted_tasks': submitted_tasks_items, 
                                               'tasks_available': tasks_available_items, 
                                               'task_total': task_total_items, 
                                               'task_factor': task_factor_items
                                               })

def add_order(request):
    form = SubmittedTasksForm
    return render(request, 'fund/add-order.html', {'form': form})