from django.shortcuts import redirect
from django.contrib import messages


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect('login')
        
        obj = self.get_object()
        if obj.id != request.user.id:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return redirect('list_users')
        
        return super().dispatch(request, *args, **kwargs)