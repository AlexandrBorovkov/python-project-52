from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.views import View

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label


class LabelListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/list_labels.html', context={
            'labels': labels,
        })


class LabelCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = LabelForm()
        return render(request, 'labels/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Метка успешно создана')
            return redirect('list_labels')
        return render(request, 'labels/create.html', {'form': form})


class LabelUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Label.objects.get(id=label_id)
        form = LabelForm(instance=label)
        return render(
            request,
            'labels/update.html',
            {'form': form, 'label_id': label_id}
            )

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Label.objects.get(id=label_id)
        form = LabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.success(request, 'Метка успешно изменена')
            return redirect('list_labels')
        return render(
            request,
            'labels/update.html',
            {'form': form, 'label_id': label_id}
            )


class LabelDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        return render(request, 'labels/delete.html', {'label_id': label_id})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Label.objects.get(id=label_id)
        try:
            if label:
                label.delete()
                messages.success(request, 'Метка успешно удалена')
        except ProtectedError:
            messages.error(
                request,
                'Невозможно удалить метку, потому что она используется'
                )
        return redirect('list_labels')
