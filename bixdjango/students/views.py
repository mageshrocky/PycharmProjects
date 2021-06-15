from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Check
from .models import Student


# Create your views here.
def welcome(request):
    return render(request, 'homepage.html', {})


def bixadmin(request):
    username = 'nisar'
    pwd = '0303'
    u = request.POST.get("user")
    p = request.POST.get("pswd")
    if request.method == 'POST':
        if u == username and p == pwd:
            return HttpResponseRedirect('/search/')
        else:
            return HttpResponseRedirect('/fail/')

    return render(request, 'login.html', {})


def student_entry(request):
    form = Check
    context = {'form': form}
    if request.method == 'POST':
        form = Check(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/send_mail/')

    return render(request, 'entry.html', context)


def search(request):

    if request.method == 'POST':
        data = request.POST.get('searchs')
        print(data)
        record = {'StudentInfo': Student.objects.all().filter(course=data)}
        print(record)
        return render(request, 'register.html', record)

    return render(request, 'search.html', {})


def fail(request):
    return HttpResponse('login failed')


def send_mail(request):
    form_class = Check  # class not a instance
    context = {'form': form_class}

    # POST REQUEST
    if request.method == 'POST':
        form = Check(request.POST)

        your_name = request.POST['your_name']
        phno = request.POST['your_mobile_no']
        contact_email = request.POST['your_email']
        course = request.POST['your_course']

        subject = "A new contact or lead - {}".format(your_name)
        content = your_name + '\n' + contact_email + '\n' + str(
            phno) + '\n' + course
        email = EmailMessage(subject, content, to=['magesh1699@gmail.com'])
        email.send()
        return HttpResponseRedirect('/created/')

    return render(request, 'email.html', context)


def created(request):
    return HttpResponse('successfully registered\nour support team will contact you soon!')
