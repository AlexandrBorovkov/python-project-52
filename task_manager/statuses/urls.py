from django.urls import path

from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusListView.as_view(), name="list_statuses"),
    path('create/', views.StatusCreateView.as_view(), name="status_create"),
    path('<int:id>/update/', views.StatusUpdateView.as_view(), name="status_update"),
    path('<int:id>/delete/', views.StatusDeleteView.as_view(), name="status_delete"),
]
