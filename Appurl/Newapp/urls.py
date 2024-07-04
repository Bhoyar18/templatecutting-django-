
from django.urls import path,include
from .views import register
from .views import registerdata
from Newapp import views

urlpatterns = [
    # path('',views.home),
    path('register/',views.register),
    path('registerdata/',views.registerdata,name='register')
]
