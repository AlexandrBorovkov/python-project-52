from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='authored_tasks'
        )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name='executed_tasks'
        )
    label = models.ManyToManyField(Label, through='TaskLabel')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
    date_added = models.DateField(auto_now_add=True)
