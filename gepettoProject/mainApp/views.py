from django.shortcuts import render


def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')

def signup(request):
    return render(request, 'signup.html')

def mypage(request):
    return render(request, 'mypage.html')

def mypage_edit(request):
    return render(request, 'mypage_edit.html')
