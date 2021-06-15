from django.urls import path
from .views import login, register, create_task
from . import views
urlpatterns = [
    path('login/', login),
    path('create_task/', create_task, name='back'),
    path('register/', register),
    path('logout/', views.logout, name='logout'),

]