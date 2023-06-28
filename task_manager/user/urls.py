from django.urls import path
from .views import UsersPageView,  CreateUserPageView, UpdateUserPageView, DeleteUserPageView


urlpatterns = [
    path("", UsersPageView.as_view(), name="users"),
    path("create/", CreateUserPageView.as_view(), name="create_user"),
    path("<int:id>/update/", UpdateUserPageView.as_view(), name="update_user"),
    path("<int:id>/delete/", DeleteUserPageView.as_view(), name="delete_user"),
]