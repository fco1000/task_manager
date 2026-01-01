from django import forms
from .models import Task,Worker

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','due_date','priority_level','completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date'}),
        }

class WorkerForm(forms.ModelForm):
    class Meta:
          model = Worker
          fields = ['name','email']