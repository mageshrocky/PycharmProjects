from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    return HttpResponse('Hey MAGESH! \n Hearty welcome to our own App')