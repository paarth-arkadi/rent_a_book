from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
    return render(request,'login.html')