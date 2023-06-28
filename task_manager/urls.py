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
from django.urls import path, include
from task_manager.views import (
    IndexPageView,
    LoginPageView, LogoutPageView,
)

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("logout/", LogoutPageView.as_view(), name="logout"),
    path("statuses/", include("task_manager.status.urls")),
    path("labels/", include("task_manager.label.urls")),
    path("users/", include("task_manager.user.urls")),
    path("tasks/", include("task_manager.task.urls")),
    path("admin/", admin.site.urls),
]
