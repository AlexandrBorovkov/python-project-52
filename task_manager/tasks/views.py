from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django_filters.views import FilterView

from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.mixins import OwnerRequiredMixin
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/list_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().select_related('status', 'author').prefetch_related('label')


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.author = User.objects.get(pk=request.user.pk)
            form.save()
            messages.success(request, f'Задача успешно создана')
            return redirect('list_tasks')
        return render(request, 'tasks/create.html', {'form': form})


class TaskUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'tasks/update.html', {'form': form, 'task_id': task_id})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Задача успешно изменена')
            return redirect('list_tasks')
        return render(request, 'tasks/update.html', {'form': form, 'task_id': task_id})


class TaskDeleteView(LoginRequiredMixin, OwnerRequiredMixin, View):
    def get_object(self):
        return Task.objects.get(id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        return render(request, 'tasks/delete.html', {'task_id': task_id})

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
            messages.success(request, f'Задача успешно удалена')
        return redirect('list_tasks')


class TaskView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["id"])
        return render(
            request,
            "tasks/show.html",
            context={
                "task": task,
            },
        )
