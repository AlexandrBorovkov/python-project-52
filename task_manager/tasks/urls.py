from django.urls import path

from task_manager.tasks import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name="list_tasks"),
    path('create/', views.TaskCreateView.as_view(), name="task_create"),
    path('<int:id>/update/', views.TaskUpdateView.as_view(), name="task_update"),
    path('<int:id>/delete/', views.TaskDeleteView.as_view(), name="task_delete"),
    path('<int:id>/', views.TaskView.as_view(), name="task_view"),
]


#  GET /tasks/ — страница со списком всех задач
#  GET /tasks/create/ — страница создания задачи
#  POST /tasks/create/ — создание новой задачи
#  GET /tasks/<int:pk>/update/ — страница редактирования задачи
#  POST /tasks/<int:pk>/update/ — обновление задачи
#  GET /tasks/<int:pk>/delete/ — страница удаления задачи
#  POST /tasks/<int:pk>/delete/ — удаление задачи
#  GET /tasks/<int:pk>/ — страница просмотра задачи
