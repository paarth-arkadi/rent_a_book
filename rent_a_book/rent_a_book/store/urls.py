from django.urls import path
from . import views

urlpatterns = [
    path('rent/createOrder',views.index4,name='store'),
    path('ezsignup',views.index3,name='store'),
    path('rent/<product_id_no>',views.index2,name='store'),
    path('info/<product_id_no>',views.index1,name='store'),
    path('',views.index,name='store'),
]