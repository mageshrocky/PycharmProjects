from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Field


# Create your views here.
def login(request):
    user = 'nisar'
    pwd = '1234'
    u = request.POST.get('username')
    p = request.POST.get('password')
    if request.method == 'POST':
        if user == u and pwd == p:
            return HttpResponseRedirect('/create_task/')

    return render(request, 'login.html', {})


def create_task(request):
    record = {'status': Field.objects.filter(status='pending')}
    if request.method == 'POST':
        return HttpResponseRedirect('/register/')
    return render(request, 'create.html', record)


def register(request):
    if request.method == 'POST':
        n = request.POST.get('names')
        r = request.POST.get('roles')
        t = request.POST.get('tasks')
        s = request.POST.get('statu')

        Field.objects.create(name=n, role=r, task=t, status=s)

        return HttpResponse('task created!')
    return render(request, 'task.html', {})


def back(request):
    return HttpResponseRedirect('/create_task/')


def logout(request):
    return HttpResponseRedirect('/login/')
