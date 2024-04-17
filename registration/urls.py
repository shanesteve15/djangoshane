from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registration, name='registration'),
    path("registerpage/", views.mypage, name='myregisterpage'),
    path("", views.home, name='home'),
    path("login/", views.login, name='login'),
    path("addstudent", views.addstudent, name='addingstudent')
]



