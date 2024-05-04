from django.urls import path
from .views import *

urlpatterns = [
    path('index/',index),
    path('',loadloginform),
    path('register/',register),
    path('login/',login),
    path('adminlogin/',adminlogin),
    path('adminregister/',adminregister),
    path('send/',send_mail_regis),
    path('verify/<auth_token>',verify),
    path('additem/',additem),
    path('showitem/',showitem),   #admin view items
    path('viewitem/',viewitem),   #user view items
    path('cart/',cart),












]