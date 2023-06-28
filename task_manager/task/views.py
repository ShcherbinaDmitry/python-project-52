from django.shortcuts import render
from django.views import View

# Create your views here.
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