from django.contrib import admin
from signup.models import myuserDetails,myshippingAddr
# Register your models here.
admin.site.register(myuserDetails)
admin.site.register(myshippingAddr)