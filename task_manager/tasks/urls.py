from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="list_tasks"),
    path('create/', views.TaskCreateView.as_view(), name="task_create"),
    path(
        '<int:id>/update/',
        views.TaskUpdateView.as_view(),
        name="task_update"
        ),
    path(
        '<int:id>/delete/',
        views.TaskDeleteView.as_view(),
        name="task_delete"
        ),
    path('<int:id>/', views.TaskView.as_view(), name="task_view"),
]
