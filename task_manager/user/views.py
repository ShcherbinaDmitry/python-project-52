from django.shortcuts import render
from django.views import View

# Create your views here.
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