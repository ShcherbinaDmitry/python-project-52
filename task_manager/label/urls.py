from django.urls import path
from .views import LabelsPageView, CreateLabelPageView, UpdateLabelPageView, DeleteLabelPageView


urlpatterns = [
    path("", LabelsPageView.as_view(), name="labels"),
    path("create/", CreateLabelPageView.as_view(), name="create_label"),
    path("<int:id>/update/", UpdateLabelPageView.as_view(), name="update_label"),
    path("<int:id>/delete/", DeleteLabelPageView.as_view(), name="delete_label"),
]