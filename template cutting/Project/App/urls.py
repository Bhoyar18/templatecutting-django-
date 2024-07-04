from django.urls import path,include
from App import views 

urlpatterns=[
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about')
]