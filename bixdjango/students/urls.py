from django.urls import path
from .views import welcome, created, search, fail, send_mail
from . import views

urlpatterns = [

    path('welcome/', welcome),
    path('bixadmin/', views.bixadmin, name='bixadmin'),
    path('student_entry/', views.student_entry, name='student_entry'),
    path('created/', created),
    path('search/', search),
    path('fail/', fail),
    path('send_mail/', send_mail),
]