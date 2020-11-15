
from django.http import HttpResponse
from django.shortcuts import render



def saludar(request):
    return HttpResponse("<h1>saludos mortales!!</h1>")


def Login(request):
    return render(request,'login.html')


def index(request):
    return render(request,'index.html')
