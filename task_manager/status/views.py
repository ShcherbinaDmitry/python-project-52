# Create your views here.
from django.shortcuts import render, redirect
from django.views import View

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