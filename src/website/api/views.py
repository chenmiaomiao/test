from django.shortcuts import render
from .models import tasks
from rest_framework import viewsets
from .Serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = tasks.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer