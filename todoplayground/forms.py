from django import forms
from django.core.exceptions import ValidationError
from .models import TodoItem
import re

class TodoItemForm(forms.ModelForm):
    task = forms.CharField(
        min_length=3,
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control w-100',
                'placeholder': 'Add new task',
            }
        ),
        error_messages={'required': 'Task is required.'}
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(TodoItemForm, self).__init__(*args, **kwargs)
        
        if instance:
            self.initial['task'] = instance.task

    class Meta:
        model = TodoItem
        fields = ['task']

    def clean_task(self):
        task = self.cleaned_data['task']
        if not re.match(r'^[a-zA-Z0-9 ]*$', task):
            raise ValidationError("Task should only contain letters and numbers.")
        return task
