# from cv2 import detail_DpSeamFinder
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from requests import request
# from .forms import userForm
from . import forms
from service.models import User




def homepage(request):
    
    return render(request,"homepage.html")
    

def aboutus(request):
    
    return render(request,"aboutus.html")
def books(request):
    mydict={'key_1':"Hello ,This Is From dictonart"}
    return render(request,"books.html",context=mydict)
def research(request):
    return render(request,"research.html")
def login(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATOIN SUCCESS")

            print("NAME  "+form.cleaned_data['name'])
            print("EMAIL  "+form.cleaned_data['email'])
            print("TEXT  "+form.cleaned_data['text'])




    return render(request,"login.html",{'form':form})
# def form_name_view(request):
    
#     return render
def signup(request):
    return render(request,"signup.html")

def userform(request):
    return render(request,"Userform.html")









# def aboutus(request):
#     return render(request,"aboutus.html")

# def books(request):
#     if request.method == "GET":
#         output = request.GET.get('output')
#     return render(request,"books.html",{"output":output})

# def research(request):
#     return render(request,"research.html")

# def homepage(request):
#     data = {
#         'title': 'Home page',
#         'bdata' : 'This is Big data',
#         'mylist' : ['Python','Html','CSS','Javascript'],
#         'num' : [10,20,30,40,50],
        
#         'details' : [
#             {'name' : "Ujjwal Srivastava",'Mob no' : 123456789},
#             {'name': "Aman pratap Singh", 'Mob no' : 987654321}
#         ]
    
#     }

#     return render(request,'homepage1.html')

# def myDetail(request,details):
#     return HttpResponse(details)

# def steve_jobs(request):
#     return render(request,"steve_jobs.html")
# def calculater(request):
#     val = 0
#     data = {}
#     try:
#         if (request.method == 'POST'):
#             n1 = eval(request.POST.get('num1'))
#             n2 = eval(request.POST.get('num2'))
#             inp = request.POST.get('opr')
#             if inp == '+':
#                 val = n1 + n2
#             elif inp == '-':
#                 val = n1 - n2
#             elif inp == '/':
#                 val = n1 / n2
#             elif inp == '*':
#                 val = n1 * n2

#         else:
#             print("Invalid sign")
#         data = {"val1":n1,"val2":n2,"output":val}
#     except:
#         pass
#     print(val)
#     return render(request,'calulater.html',data)

    
# def userform(request):
#     var = 0
#     fn = userForm()
#     data = {'form':fn}
#     try:
#         if (request.method == "POST"):
#             # n1 = int(request.GET['num1'])
#             # n2 = int(request.GET['num2'])
#             n1 = int(request.POST.get('num1'))
#             n2 = int(request.POST.get('num2'))
            
#             var = n1+ n2
#             url = "/books/?output={}".format(var)
#             data = { 'form': fn ,'output': var }

#             return HttpResponseRedirect(url)
#     except:
#         pass


#     return render(request,"userform.html",data)

