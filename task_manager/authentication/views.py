from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from task_manager.authentication.forms import LoginForm


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        messages.success(self.request, 'Вы залогинены')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
