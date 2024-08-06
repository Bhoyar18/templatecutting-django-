from django.shortcuts import render

# Create your views here.

#  type 1 = by passing only key and provide the name of key
# def home(request):
#     Name ='Vaishnavi bhoyar'
#     City ='Bhopal'
#     Qualification = 'B.Tech'

#     return render(request,'home.html',{'nm':Name,
#                                        'ct':City,
#                                        'qual':Qualification
#                                        })

# ===========================================================================================

# type 2 =  passing key and value in dictionary format
# def home(request):
#     data={
#         'nm':'Vaishnavi bhoyar',
#         'ct':'Bhopal',
#         'qual':'B.tech'
#      }
#     return render(request,'home.html',{'key':data})

# =========================================================================================

# type 3 = passing one attribute in like nm in all place
# def home(request):
#     data={
#         'nm':{
#             'name':"Vaishnavi bhoyar",
#             'ct':"Bhopal",
#             'qual':"B.tech"
#         } 
#      }
#     return render(request,'home.html',{'key':data})

# ============================================================================================ 
