from django import forms
from .models import Task, Board
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', ]

        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Wpisz nowe zadanie'}),
        }


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['board_name']

        widgets = {
            'board_name': forms.TextInput(attrs={'class': 'form-field', 'placeholder': 'Wpisz nazwę nowej tablicy'})
        }
