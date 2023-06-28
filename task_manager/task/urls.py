from django.urls import path
from .views import TasksPageView, CreateTaskPageView, UpdateTaskPageView, DeleteTaskPageView


urlpatterns = [
    path("", TasksPageView.as_view(), name="tasks"),
    path("create/", CreateTaskPageView.as_view(), name="create_task"),
    path("int:id>/update/", UpdateTaskPageView.as_view(), name="update_task"),
    path("<int:id>/delete/", DeleteTaskPageView.as_view(), name="delete_task"),
]