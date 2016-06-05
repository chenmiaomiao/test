from django import forms
from .models import new_account

class NewAccount(forms.ModelForm):
    
    class Meta:
        model = new_account
        fields = ['id_front', 'id_back', 'id_number', 'phone_number', 'password', 'verification_code']