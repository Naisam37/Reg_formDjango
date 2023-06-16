from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not uname or not email or not pass1 or not pass2:
            return HttpResponse("Please fill in all the fields.")



        if pass1 != pass2:
            return HttpResponse("Your password and confirm password do not match.")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')



def Login (request) :
    
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        
        if user is not None :
            login(request,user)
            return redirect('home')
        else:
           return  HttpResponse ("Username or Password is incorrect!!!")
           
    return render (request,'login.html')

def LogOut(request) :
    logout(request)
    return redirect('login')





