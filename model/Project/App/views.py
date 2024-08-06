from django.shortcuts import render

# Create your views here.
from .models import *
def home(request):
    # data=Student.objects.all()
    # for printing the one value like name from table   
    # print(data)
    # for printing all values of table
    # print(data.values())
    # data=Student.objects.last()

    # get(coloumn_name=value)
    data0=Student.objects.get(id=3)
    print(data0)
    print(data0.id,data0.Stu_Name,data0.Stu_Email)
    # return HttpResponse(data0)

    # first
    # data0=Student.objects.first()
    # data0=Student.objects.order_by('Stu_Name').first()
    #  #for descending order
    # # data0=Student.objects.order_by('-Stu_Name').first() 
    # print(data0.id,data0.Stu_Name,data0.Stu_Email)
    # # return HttpResponse(data0)


    #last
    # data0=Student.objects.last()
    # data0=Student.objects.order_by('-Stu_Name').last()
    # print(data0.id,data0.Stu_Name,data0.Stu_Email)

    # for creating one more table we use create
    # create(coloumn1=value1,coloumn2=value2)
    data0=Student.objects.create(Stu_Name='Maanu',Stu_Email='manu02@gmail.com',Stu_Contact='1234567',
    Stu_City='Pune')
    print(data0.id,data0.Stu_Name,data0.Stu_Email,data0.Stu_Contact,data0.Stu_City)

    # get or create
    # data0 ,created=Student.objects.get_or_create(Stu_Name='Maanu',Stu_Email='manu02@gmail.com',Stu_Contact='987654321',
    # Stu_City='Pune')
    # print(data0.id,data0.Stu_Name,data0.Stu_Email,data0.Stu_Contact,data0.Stu_City)
    # print(created)







    return render(request,'home.html')