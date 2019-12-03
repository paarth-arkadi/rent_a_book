from django.db import models

# Create your models here.
class myuserDetails(models.Model):
    udemailid = models.CharField(max_length=254,default="")
    phoneNumber = models.IntegerField()
    ageOfChild = models.IntegerField()
    genderOfChild = models.CharField(max_length=1) #Whether 'M' or 'F'
    memType = models.CharField(max_length=1) #Whether 'P' For permenant or 'R' Regular
    invalid = models.CharField(max_length=1)

class myshippingAddr(models.Model):
    # Here p stands for permenant and d stands for delivery
    #usershippingId = models.ForeignKey(userDetails,on_delete=models.CASCADE,default=none)
    sdemailid = models.CharField(max_length=254,default="")
    pAddressLine1 = models.CharField(max_length=100)
    pAddressLine2 = models.CharField(max_length=100)
    pCity = models.CharField(max_length=100)
    pState = models.CharField(max_length=100)
    pZip = models.IntegerField()
    dAddressLine1 = models.CharField(max_length=100)
    dAddressLine2 = models.CharField(max_length=100)
    dCity = models.CharField(max_length=100)
    dState = models.CharField(max_length=100)
    dZip = models.IntegerField()