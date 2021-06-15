from django.urls import path

from . import views
from .views import display, empview, created, search, send_mail, submit, register

urlpatterns = [
    path('display/', display),
    path('empview/', empview),
    path('created/', created),
    path('search/', search),
    path('send_mail/', send_mail),
    path('submit/', submit),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login')
    #path('loginpage/', views.loginpage, name='login'),
    #path('register/', views.register, name='register'),
]