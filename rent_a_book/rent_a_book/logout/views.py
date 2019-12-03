from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
# Create your views here.
def index(request):
    auth.logout(request)
    return redirect("/")