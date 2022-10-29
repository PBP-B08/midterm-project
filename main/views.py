from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import Profile

# @login_required(login_url='main:login')
def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("main:index"))
            response.set_cookie('last_login', str(date.today()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='main:login')
def profile(request):
    # display user profile info
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(id=request.user.id)
    if profile.city == None:
        profile.city = ""
    if profile.occupation == None:
        profile.occupation = ""
    if profile.name == None:
        profile.name = ""

    context = {'username':user,
                'name': profile.name,
                'city': profile.city,
                'occupation': profile.occupation,
                }
    return render(request, 'profile.html', context)

@login_required(login_url='main:login')
def update_profile(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user.id)
        name = request.POST.get("name")
        occupation = request.POST.get("occupation")
        city = request.POST.get("city")

        # update profile information
        if name:
            profile.name = name
        if occupation:
            profile.occupation = occupation
        if city:
            profile.city = city

        profile.save()        
        return redirect("main:profile")