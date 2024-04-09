from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path("registerpage/", views.mypage, name='myregisterpage'),
    path("home/", views.home, name='home'),
    path("login/", views.login, name='login'),
]