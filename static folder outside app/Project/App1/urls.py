from django.urls import path,include
from App1 import views

urlpatterns=[
    path('',views.home,name='home'),
]