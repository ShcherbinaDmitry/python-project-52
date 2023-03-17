"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_manager.views import (
    IndexPageView,
    LoginPageView,
    UsersPageView,  CreateUserPageView, UpdateUserPageView, DeleteUserPageView,
    StatusesPageView, CreateStatusPageView, UpdateStatusPageView, DeleteStatusPageView,
    LabelsPageView, CreateLabelPageView, UpdateLabelPageView, DeleteLabelPageView,
    TasksPageView, CreateTaskPageView, UpdateTaskPageView, DeleteTaskPageView,
)

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("users/", UsersPageView.as_view(), name="users"),
    path("users/create/", CreateUserPageView.as_view(), name="create_user"),
    path("users/<int:id>/update/", UpdateUserPageView.as_view(), name="update_user"),
    path("users/<int:id>/delete/", DeleteUserPageView.as_view(), name="delete_user"),
    path("statuses/", StatusesPageView.as_view(), name="statuses"),
    path("statuses/create/", CreateStatusPageView.as_view(), name="create_status"),
    path("statuses/<int:id>/update/", UpdateStatusPageView.as_view(), name="update_status"),
    path("statuses/<int:id>/delete/", DeleteStatusPageView.as_view(), name="delete_status"),
    path("labels/", LabelsPageView.as_view(), name="labels"),
    path("labels/create/", CreateLabelPageView.as_view(), name="create_label"),
    path("labels/<int:id>/update/", UpdateLabelPageView.as_view(), name="update_label"),
    path("labels/<int:id>/delete/", DeleteLabelPageView.as_view(), name="delete_label"),
    path("tasks/", TasksPageView.as_view(), name="tasks"),
    path("tasks/create/", CreateTaskPageView.as_view(), name="create_task"),
    path("tasks/<int:id>/update/", UpdateTaskPageView.as_view(), name="update_task"),
    path("tasks/<int:id>/delete/", DeleteTaskPageView.as_view(), name="delete_task"),
    path("admin/", admin.site.urls),
]
