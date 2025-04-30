from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.views import View

from task_manager.users.forms import UserForm
from task_manager.users.mixins import OwnerRequiredMixin
from task_manager.users.models import User


class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/list_users.html', context={
            'users': users,
        })


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
        return render(request, 'users/register.html', {'form': form})


class UserUpdateView(OwnerRequiredMixin, View):
    def get_object(self):
        return User.objects.get(id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(
            request,
            'users/user_update.html',
            {'form': form, 'user_id': user_id}
            )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('list_users')

        return render(
            request,
            'users/user_update.html',
            {'form': form, 'user_id': user_id}
            )


class UserDeleteView(OwnerRequiredMixin, View):
    def get_object(self):
        return User.objects.get(id=self.kwargs.get('id'))

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        return render(request, 'users/user_delete.html', {'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        try:
            if user:
                user.delete()
                messages.success(request, 'Пользователь успешно удален')
        except ProtectedError:
            messages.error(
                request,
                'Невозможно удалить пользователя, потому что он используется'
                )
        return redirect('list_users')
