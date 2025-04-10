from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusListView(View):
     def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/list_statuses.html', context={
            'statuses': statuses,
        })


class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            messages.success(request, f'Создан статус {status}!')
            return redirect('list_statuses')
        return render(request, 'statuses/create.html', {'form': form})


class StatusUpdateView(View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(request, 'statuses/update.html', {'form': form, 'status_id': status_id})
    
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('list_statuses')
        return render(request, 'update.html', {'form': form, 'status_id': status_id})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        return render(request, 'statuses/delete.html', {'status_id': status_id})
    
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        if status:
            status.delete()
        return redirect('list_statuses')
