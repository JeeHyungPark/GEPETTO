from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
import os, sys
import random
import requests


def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            if 'nickname' in request.POST:
                nickname = request.POST['nickname']
                password = request.POST['password']
                user = authenticate(request, nickname=nickname, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('login')
                else:
                    return render(request, 'testApp/input.html')
        return render(request, 'login.html')
    else:
        return render(request, 'testApp/input.html')

def main(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['email'], request.POST['nickname'], request.POST['password'])
        user.gender = request.POST['gender']
        user.age = request.POST['age']
        user.save
        return render(request, 'login.html')
    return render(request, 'signup.html')

def mypage(request):
    user = request.user
    username = request.user.nickname
    return render(request, 'mypage.html', {'user':user, 'username':username})

def mypage_edit(request):
    return render(request, 'mypage_edit.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
