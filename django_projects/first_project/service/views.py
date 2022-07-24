from django.shortcuts import render
# from django.http import HttpResponse
# from . import forms
from service.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'first_project/templates/homepage.html')


def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("FORM IS INVALID")

    return render(request,'User')
