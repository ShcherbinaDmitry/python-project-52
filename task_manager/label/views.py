from django.shortcuts import render
from django.views import View

# Create your views here.
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