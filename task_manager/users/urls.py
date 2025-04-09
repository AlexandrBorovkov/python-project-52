from django.urls import path

from task_manager.users import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name="list_users"),
    path('create/', views.UserCreateView.as_view(), name="user_create"),
    path('<int:id>/update/', views.UserUpdateView.as_view(), name="user_update"),
    path('<int:id>/delete/', views.UserDeleteView.as_view(), name="user_delete"),
]



#  GET /users/ — страница со списком всех пользователей
#  GET /users/create/ — страница регистрации нового пользователя
#  POST /users/create/ — создание пользователя
#  GET /users/<int:pk>/update/ — страница редактирования пользователя
#  POST /users/<int:pk>/update/ — обновление пользователя
#  GET /users/<int:pk>/delete/ — страница удаления пользователя
#  POST /users/<int:pk>/delete/ — удаление пользователя