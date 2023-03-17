from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


# Index page
class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# Login page
class LoginPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


    def post(request, **kwargs):
        return None


# Users views
class UsersPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/index.html')

class CreateUserPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(request, **kwargs):
        return None

class UpdateUserPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/update.html')

    def post():
        return None

class DeleteUserPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/delete.html')
    
    def post():
        return None


# Statuses views
class StatusesPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/index.html')
    
class CreateStatusPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/create.html')

    def post():
        return None

class UpdateStatusPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/update.html')

    def post():
        return None

class DeleteStatusPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/delete.html')

    def post():
        return None

# Labels views
class LabelsPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'labels/index.html')
    
class CreateLabelPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'labels/create.html')

    def post():
        return None

class UpdateLabelPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'labels/update.html')
    
    def post():
        return None

class DeleteLabelPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'labels/delete.html')
    
    def post():
        return None


# Tasks views
class TasksPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')
    
class CreateTaskPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/create.html')

    def post():
        return None

class UpdateTaskPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/update.html')

    def post():
        return None

class DeleteTaskPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/delete.html')

    def post():
        return None