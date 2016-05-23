from django.shortcuts import render
from .forms import SubmittedTasksForm

# Create your views here.

def index(request):
    return render(request, 'fund/index.html')

def add_order(request):
    form = SubmittedTasksForm
    return render(request, 'fund/add-order.html', {'form': form, })