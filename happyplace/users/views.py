from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


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

