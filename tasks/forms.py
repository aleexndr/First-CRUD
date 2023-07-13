from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'importante']
        widgets =  {
            'titulo': forms.TextInput(attrs={'class': 'form-control form-floating'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control' }),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input' }),
        }