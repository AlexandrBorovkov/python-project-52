from django.contrib import messages
from django.shortcuts import redirect


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author_id != request.user.id:
            messages.error(request, 'Задачу может удалить только ее автор')
            return redirect('list_tasks')
        return super().dispatch(request, *args, **kwargs)
