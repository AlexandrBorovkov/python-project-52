from django.urls import path

from task_manager.users import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name="list_users"),
    path('create/', views.UserCreateView.as_view(), name="user_create"),
    path('<int:id>/update/', views.UserUpdateView.as_view(), name="user_update"),
    path('<int:id>/delete/', views.UserDeleteView.as_view(), name="user_delete"),
]
