from django.contrib.auth.password_validation import password_changed
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, "home.html")


def loginuser(request):
    return render(request, "login.html")


def signupuser(request):
    print(f"POST : {request.POST}")
    if request.method == "POST":
        uname = request.POST.get("id_username")
        pass1 = request.POST.get("id_password1")
        pass2 = request.POST.get("id_password2")
        print(f"uname: {uname}, pwd: {pass1}, pwd2: {pass2}")
        if User.objects.filter(username__iexact=uname).exists():
            messages.error(
                request,  "This  Username is  already exist please try another email")
            return redirect('/signup/')
        else:
            if pass1 == pass2:
                User.objects.create_user(
                    username=uname, password=pass1)
                messages.success(
                    request, 'Congratulations you have registered successfully ')
                return redirect('')
            else:
                messages.error(
                    request,  "The password confirmation does not match with password.")
                return redirect('/')
    return render(request, "signup.html")
