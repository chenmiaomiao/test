from django import forms
from .models import submitted_tasks

class SubmittedTasksForm(forms.ModelForm):
    
    class Meta:
        model = submitted_tasks
        fields = ['employee_id', 'client_id', 'order_quantity', 'order_date', 'register_date']