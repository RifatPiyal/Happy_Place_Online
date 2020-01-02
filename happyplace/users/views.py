from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# SH
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # using Django UserRegistrationForm
        if form.is_valid():
            form.save()  # if the form is valid than save it to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('/login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})  # if form invalid than redirect to register.html


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


# SH
def group_check(request):
    group_name = Group.objects.all().filter(user=request.user)  # get logget user grouped name
    group_name = str(group_name[0])  # convert to string

    if "Student" == group_name:
        return redirect('http://127.0.0.1:8000/student/')
    elif "Teacher" == group_name:
        return redirect('http://127.0.0.1:8000/teacher/')


def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')


class register_teacher(TemplateView):
    template_name = "register_teacher.html"


class register_student(TemplateView):
    template_name = "register_student.html"
