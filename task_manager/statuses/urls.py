from django.urls import path

from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusListView.as_view(), name="list_statuses"),
    path('create/', views.StatusCreateView.as_view(), name="status_create"),
    path('<int:id>/update/', views.StatusUpdateView.as_view(), name="status_update"),
    path('<int:id>/delete/', views.StatusDeleteView.as_view(), name="status_delete"),
]


#  GET /statuses/ — страница со списком всех статусов
#  GET /statuses/create/ — страница создания статуса
#  POST /statuses/create/ — создание нового статуса
#  GET /statuses/<int:pk>/update/ — страница редактирования статуса
#  POST /statuses/<int:pk>/update/ — обновление статуса
#  GET /statuses/<int:pk>/delete/ — страница удаления статуса
#  POST /statuses/<int:pk>/delete/ — удаление статуса