from .models import student3
from django import forms


class UserRegisterationForm(forms.ModelForm):

    class Meta:
        model = student3
        fields = ['name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),

        }


