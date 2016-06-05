from django.shortcuts import render
from .forms import NewAccount

def index(request):
    return render(request, 'csc108/index.html', {})

def video(request):
    return render(request, 'csc108/video.html',{})