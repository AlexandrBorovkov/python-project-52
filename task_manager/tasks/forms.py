from django import forms

from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
            'label': 'Метки'
            }
        widgets = {
            'label': forms.SelectMultiple(attrs={'class': 'form-select'})
        }
