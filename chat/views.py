from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import random


# Create your views here.
def chat(request):
    return render(request, 'chat.html', {})


def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("try")
        return render(request,'login.html', {})


def signup(request,):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password']
            confirm_password = request.POST['confirm_password']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            if password1 == confirm_password:
                if len(password1) > 8:
                    error = True
                else:
                    error = False
                if error == True:
                    user = User.objects.create_user(username=username, email=email, password=password1,
                                                    first_name=first_name, last_name=last_name)
                    if user:
                        return redirect("login")
                else:
                    error = "Please use more than 8"
                    print(error)
                    return render(request, 'signup.html', {'error': error})
            else:
                error = "Password not Match"
                print(error)
                return render(request, 'signup.html', {'error': error})
        return render(request, 'signup.html', {})


def Logout(request):
    logout(request)
    #  return redirect("index")
    return render(request, 'l.html', {})


# def get(request):
#  user=User.objects.all()
#  return render(request,'try.html')
def get(request,self):
    stud = User.objects.all()
    print('myoutput', stud)
    return render(request, 'data.html', {'stu': stud})


