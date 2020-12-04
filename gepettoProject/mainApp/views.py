from django.shortcuts import render, redirect
import os, sys
import random
import requests
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login,authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import User
from django.db.models import Q
from testApp.models import Test

def main(request):
    return render(request, 'main.html')

class SignupView(FormView):
    """sign up user view"""
    form_class = forms.SignupForm
    template_name = 'signup.html'
    success_url = 'http://127.0.0.1:8000/test'

    def form_valid(self, form):
        """ process user signup"""
        user = form.save(commit=False)
        user.save()
        
        print(user.nickname)
        print(user.email)
        print(user.password)
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)


class LoginView(FormView):
    """login view"""

    form_class = forms.LoginForm
    success_url = 'http://127.0.0.1:8000/test'
    template_name = 'login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data
        queryset = User.objects.all()
        user = queryset.filter(email=credentials['email'], password=credentials['password'])
        print(queryset)
        #print(user[0])

        if user is not None:
            login(self.request, user[0])
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect('http://127.0.0.1:8000/login')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/')

def mypage(request):
    cur_user = request.user

    if cur_user.is_authenticated: 
        user = cur_user
        queryset = Test.objects.values()
        test_sample = queryset.filter(tester=user)
        samples = test_sample
        return render(request, 'mypage.html', {'user':user, 'samples':samples})

    else:
        return redirect('main')

def mypage_edit(request):
    return render(request, 'mypage_edit.html')

