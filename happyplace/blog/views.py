from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#  request and the html files locations to render


def home(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/Contact.html')


def FAQ(request):
    return render(request, 'blog/FAQ.html')


def advice(request):
    return render(request, 'blog/advice.html')


def login(request):
    return render(request, 'blog/login.html')


def individual(request):
    return render(request, 'blog/Quesform.html')


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


def c_dashboard(request):
    return render(request, 'blog/Cdashboard.html')


def loginCounselor(request):
    return render(request, 'blog/loginCounselor.html')
