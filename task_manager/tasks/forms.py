from django import forms

from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        labels = {'name': 'Имя', 'description': 'описание', 'status': 'статус', 'executor': 'исполнитель', 'label': 'метки'}
