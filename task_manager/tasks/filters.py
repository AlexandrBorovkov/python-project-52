import django_filters


from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус'
    )
    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
    )
    user = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Исполнитель'
    )

    class Meta:
        model = Task
        fields = ['status', 'label', 'executor']