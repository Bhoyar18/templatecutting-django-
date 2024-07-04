from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def contact(request):
    return HttpResponse("Welcome to our Contact page...")

