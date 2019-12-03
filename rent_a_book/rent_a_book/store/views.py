from django.shortcuts import render
from store.models import EcomProduct,Orders
from signup.models import myuserDetails,myshippingAddr
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    product = EcomProduct.objects.all()
    user = User.objects.all()
    return render(request,'store.html',{'product':product})

def index1(request,product_id_no):
    product = EcomProduct.objects.all().filter(id=product_id_no)
    print(product)
    return render(request,'mystore.html',{'product':product})

def index2(request,product_id_no):
    # This is used for final checkout
    product = EcomProduct.objects.all().filter(id=product_id_no)
    # This is the logged in user
    current_user = request.user
    useremail = current_user.email
    current_user_details = myuserDetails.objects.all().filter(udemailid=useremail)
    current_user_shipping = myshippingAddr.objects.all().filter(sdemailid=useremail)   
    return render(request,'checkout.html',{'product':product,'current_user':current_user,'current_user_shipping':current_user_shipping},{'current_user_details':current_user_details})

def index3(request):
    return render(request,'ezsignup.html')

def index4(request):
    current_user = request.user
    useremail = current_user.email
    order = Orders.objects.create(odemailid= useremail)
    order.save()
    index = order.id
    email = order.odemailid
    todayDate = order.purchaseDate
    deliveryDate = order.deliveryDate
    returnDate = order.returnDate
    if order != None:
        messages.info(request,'Order Created SuccessFully')
    else:
        messages.info(request,'Order Not Created')
    return render(request,'createOrder.html',{'email':email,'todayDate':todayDate,'deliveryDate':deliveryDate,'returnDate':returnDate,'index':index})