from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from task_manager.users.forms import UserForm
from task_manager.users.models import User
from task_manager.users.mixins import OwnerRequiredMixin


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
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно зарегистрирован')
            return redirect('login')
        return render(request, 'users/register.html', {'form': form})


class UserUpdateView(OwnerRequiredMixin, View):
    def get_object(self):
        return User.objects.get(id=self.kwargs.get('id'))
    
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(request, 'users/user_update.html', {'form': form, 'user_id': user_id})
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Пользователь успешно изменен')
            return redirect('list_users')

        return render(request, 'users/user_update.html', {'form': form, 'user_id': user_id})


class UserDeleteView(OwnerRequiredMixin, View):
    def get_object(self):
        return User.objects.get(id=self.kwargs.get('id'))
    
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        return render(request, 'users/user_delete.html', {'user_id': user_id})
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            messages.success(request, f'Пользователь успешно удален')
        return redirect('list_users')
