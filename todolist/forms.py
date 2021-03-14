from django import forms
from .models import TaskList

class TaskFrom(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task','done']
