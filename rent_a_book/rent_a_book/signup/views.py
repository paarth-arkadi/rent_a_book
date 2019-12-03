from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from signup.models import myuserDetails,myshippingAddr
# Create your views here.
def index(request):
    if request.method == "POST":
        # user auth credentials
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        # user details
        phoneNumber = request.POST['phone_number']
        ageOfChild = request.POST['age_of_child']
        genderOfChild = request.POST['gender_of_child']
        memType = request.POST['membership_type']
        # user Shipping Details
        pAddressLine1 = request.POST['p_addr_line_1']
        pAddressLine2 = request.POST['p_addr_line_2']
        pCity = request.POST['p_addr_city']
        pState = request.POST['p_addr_state']
        pZip = request.POST['p_addr_zip']
        dAddressLine1 = request.POST['d_addr_line_1']
        #dAddressLine2 = request.POST['d_addr_line_2']
        dCity = request.POST['d_addr_city']
        dState = request.POST['d_addr_state']
        dZip = request.POST['d_addr_zip']

        if password!=confirm_password:
            messages.info(request,"Password Not Matching")
            return render(request,'signup.html')
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Taken")
            return render(request,'signup.html')
        
        user_auth = User.objects.create_user(username=email,email=email,password=password,first_name=first_name,last_name=last_name)
        user_auth.save()
        
        if genderOfChild == "Male":
            genderOfChild = 'M'
        else:
            genderOfChild = 'F'
        if memType == "Premium":
            memType = 'P'
        else:
            memType = 'R'
        user_details = myuserDetails.objects.create(udemailid=email,phoneNumber=phoneNumber,ageOfChild=ageOfChild,genderOfChild=genderOfChild,memType=memType,invalid=0)
        user_details.save()

        shipping_details = myshippingAddr.objects.create(sdemailid=email,pAddressLine1=pAddressLine1,pAddressLine2=pAddressLine2,pCity=pCity,pState=pState,pZip=pZip,dAddressLine1=dAddressLine1,dCity=dCity,dState=dState,dZip=dZip)
        shipping_details.save()
        if user_auth == None or user_details == None or shipping_details==None:
            messages.info(request,"User not created")
            return render(request,'signup.html')

        messages.info(request,"Thank You {0}! You have been registered successfully.".format(first_name))
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect("/")