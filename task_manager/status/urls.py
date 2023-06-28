from django.urls import path
from .views import StatusesPageView, CreateStatusPageView, UpdateStatusPageView, DeleteStatusPageView


urlpatterns = [
    path("", StatusesPageView.as_view(), name="statuses"),
    path("create/", CreateStatusPageView.as_view(), name="create_status"),
    path("<int:id>/update/", UpdateStatusPageView.as_view(), name="update_status"),
    path("<int:id>/delete/", DeleteStatusPageView.as_view(), name="delete_status"),
]