from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class IndexPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
    
class LoginPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
    
class LogoutPageView(View):
    def get(self, request, *args, **kwargs):
        return redirect("/")