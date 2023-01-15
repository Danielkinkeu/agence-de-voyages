from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

# Create your views here.

# def login_form(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pwd = request.POST["pwd"]
#         print('le nom est:', username,pwd)
#         user = authenticate(username=username, password=pwd)
#         if user is not None:
#             return redirect("home")
#         else:
#             messages.error(request,"Erreur d'authentification")
#             return render(request, 'login_form.html',) 
#     return render(request, "login_form.html")

def login_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            print(username)
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request,user)
                if username=='vabus' and pwd=='BUS':
                    return redirect('index')
                else:
                    return redirect('home')
            else:
                messages.error(request,"Mot de passe ou nom de utilisateur incorrect !") 
                return render(request , 'login_form.html', {'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] +='is-invalid'
            return render(request , 'login_form.html', {'form':form})
    else:
        form = LoginForm()
        return render(request,"login_form.html",{"form":form})
    
    
def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            pwd_confirm = form.cleaned_data['pwd_confirm']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=pwd, email=email )
            if user is not None:
                if pwd == pwd_confirm:
                    return redirect("login_form")
                else:
                   messages.error(request," les mots de passe doivent etre identiques")
                   return render(request,'register_form.html', {'form':form})  
            else:
                messages.error(request,'creation de compte echouer ')
                return render(request,'register_form.html', {'form':form})
        else:
            return render(request,'register_form.html', {'form':form})    
        return render(request,'register_form.html',{})
    form = RegisterForm()
    return render(request,'register_form.html',{'form':form})
    

def logout_form(request):
    logout(request)
    return redirect('login_form')