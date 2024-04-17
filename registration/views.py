from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader  #Create your views here. #for routing ur templates

from django.views.decorators.csrf import csrf_exempt

from .models import student


def registration(request):
    return HttpResponse("Welcome to the registration")

def mypage(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
   # return HttpResponse(template.render())
    return render(request, 'login.html')

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('mail')
        password = request.POST.get('word')
        country="kenya"
        mydata = {'name': name, 'email': email, 'password': password}
        print(mydata)
        query = student(first_name=name, email=email,password=password,country=country)
        query.save()
   #fetch the student data to be displayed
    #data = student.objects.all()
   # context = {'data': data}
    return render(request, 'register.html')
