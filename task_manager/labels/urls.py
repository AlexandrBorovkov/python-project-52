from django.urls import path

from task_manager.labels import views


urlpatterns = [
    path('', views.LabelListView.as_view(), name="list_labels"),
    path('create/', views.LabelCreateView.as_view(), name="label_create"),
    path('<int:id>/update/', views.LabelUpdateView.as_view(), name="label_update"),
    path('<int:id>/delete/', views.LabelDeleteView.as_view(), name="label_delete"),
]


#  GET /labels/ — страница со списком всех меток
#  GET /labels/create/ — страница создания метки
#  POST /labels/create/ — создание новой метки
#  GET /labels/<int:pk>/update/ — страница редактирования метки
#  POST /labels/<int:pk>/update/ — обновление метки
#  GET /labels/<int:pk>/delete/ — страница удаления метки
#  POST /labels/<int:pk>/delete/ — удаление метки