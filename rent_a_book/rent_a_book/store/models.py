from django.db import models
from datetime import date
from datetime import timedelta
from django.utils import timezone
class EcomProduct(models.Model):
	name = models.CharField(max_length=255)
	imageurl = models.ImageField(upload_to='',null=True,blank=True)
	author = models.CharField(max_length = 400)
	category = models.CharField(max_length = 200)
	description = models.TextField(max_length=255)

class Orders(models.Model):
	odemailid = models.CharField(max_length=255)
	purchaseDate = models.DateTimeField(default = date.today())
	deliveryDate = models.DateTimeField(default= (date.today()+timedelta(days=3)))
	returnDate = models.DateTimeField(default=(date.today()+timedelta(days=14)))