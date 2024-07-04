from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Student
# def home(request):
#     # return HttpResponse("<h1 style='color:lightblue'>Welcome to our Newapp...</h1>")
#     data = {
#     "name":"Vaishu",
#     "age":"22",
#     "qualification":"B.tech",
#     "training":"cybrom"
#     }
#     return JsonResponse(data)


# def home(request):
#     return redirect ('https://www.shiksha.com/online-courses/articles/understanding-python-methods')


def register(request):
    return render(request,'register.html')

def registerdata(request):
    print(request.method)
    print(request.POST)
    var1=request.POST.get('email')
    var2=request.POST.get('psw')
    var3=request.POST.get('psw-repeat')

    Student.objects.create(Email=var1,Password=var2,RepeatPassword=var3)
    print("Data saved successfully...")

