from django.core.mail import EmailMessage

from employee.models import Employee, Employeeforms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Magesh, CreateUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def display(request):
    return HttpResponse('welcome to BIX IT ACADEMY')


def register(request):
    form = CreateUser
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/loginpage/')
    return render(request, 'regist.html', context)


def loginpage(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        a = authenticate(request, username=u, password=p)
        if a is not None:
            login(request, a)
            return HttpResponseRedirect('/empview/')

    context = {}
    return render(request, 'login.html', context)


def empview(request):
    form = Magesh
    context = {'form': form}
    if request.method == 'POST':
        form = Magesh(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/created/')
        else:
            print('not valid')

    return render(request, 'employee.html', context)


def created(request):
    return HttpResponse("Data created")


def search(request):
    if request.method == 'POST':
        data = request.POST.get('searchs')
        record = {'employeeInfo': Employeeforms.objects.all().filter(job=data)}
        print(record)
        return render(request, 'register.html', record)

    return render(request, 'search.html', {})


# Today,s day two
def send_mail(request):
    form_class = Magesh  # class not a instance
    context = {'form': form_class}

    # POST REQUEST
    if request.method == 'POST':
        form = Magesh(request.POST)

        your_name = request.POST['your_name']
        phno = request.POST['your_mobile_no']
        contact_email = request.POST['your_email']
        course = request.POST['your_course']

        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + contact_email + '\n' + str(
            phno) + '\n' + course
        email = EmailMessage(subject, content, to=['magesh1699 @gmail.com'])
        email.send()
        return HttpResponseRedirect('/submit/')

    return render(request, 'email.html', context)


def submit(request):
    return HttpResponse("Thank you and Have a great day!!!,I will inform soon")
