from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


