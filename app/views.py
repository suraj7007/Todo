from django import forms
from django.contrib.auth.password_validation import password_changed
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import TODO
from .forms import Todoform

# Create your views here.


@login_required(login_url='login')
def home(request):
    print(request.user)
    messages.success(request, 'Logged in successfully')
    form = Todoform()
    todo_obj = TODO.objects.filter(user=request.user)
    context = {"form":form, "todo":todo_obj}
    return render(request, "home.html", context)


@login_required(login_url="login")
def addtodo(request):
    if request.method == "POST":
        form = Todoform(request.POST)
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect("/")
    else:
        form = Todoform()
        messages.error(request, "Invalid Info")
        context = {"form":form}
        return redirect("/")


def loginuser(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user_auth = authenticate(username=uname, password=pwd)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('home')
        else:
            messages.error(
                request, 'Entered username or password is incorrect')
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect('login')


def signupuser(request):
    if request.method == "POST":
        uname = request.POST.get("id_username")
        pass1 = request.POST.get("id_password1")
        pass2 = request.POST.get("id_password2")
        if User.objects.filter(username__iexact=uname).exists():
            messages.error(
                request, "This  Username is  already exist please try another email")
            return redirect('signup')
        else:
            if pass1 == pass2:
                User.objects.create_user(
                    username=uname, password=pass1)
                messages.success(
                    request, 'Congratulations you have registered successfully')
                return redirect('login')
            else:
                messages.error(
                    request, "The password confirmation does not match with password.")
                return redirect('signup')
    return render(request, "signup.html")
