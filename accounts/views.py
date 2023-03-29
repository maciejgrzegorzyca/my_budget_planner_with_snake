from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from .forms import CreateUserForm


def login_page(request):
    # return HttpResponse("login page")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'email or password incorrect')
            return redirect('login')

    else:
        return render(request, 'planner/accounts/templates/login.html', {})


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'planner/accounts/templates/register.html', context)
    # return HttpResponse("user register page")


def logout_page(request):
    return redirect('login')
