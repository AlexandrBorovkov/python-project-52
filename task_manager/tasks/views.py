from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskListView(LoginRequiredMixin, View):
     def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/list_tasks.html', context={
            'tasks': tasks,
        })


class TaskCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'tasks/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.author = User.objects.get(pk=request.user.pk)
            task = form.save()
            messages.success(request, f'Создана задача {task}!')
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
            return redirect('list_tasks')
        return render(request, 'update.html', {'form': form, 'task_id': task_id})


class TaskDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        return render(request, 'tasks/delete.html', {'task_id': task_id})
    
    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
        return redirect('list_tasks')

class TaskView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["id"])
        return render(
            request,
            "tasks/show.html",
            context={
                "task": task,
            },
        )