from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from website.forms import CreateUserForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Reena import settings
from django.contrib.auth.models import User
from datetime import date
from django.core import serializers



######################## SignUp Views ##########################
def Signup_view(request):
    form = CreateUserForm()

    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    print(username)
    print(email)

    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for "+ user+ " succesfully")
            # response = JsonResponse({"success":True})
            return redirect("/")

        else:
            print("Invalid Form", form.errors)
            response = JsonResponse({"error":form.errors})
            response.status_code = 403
            return response
            
    return render(request, 'website/login.html', {'form':form})

######################## Login Views ##########################

def Login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email).username
            print("Username: ", username)
        except:
            username = None
        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = username
            
            if user.is_superuser:
                print("Login Done")
                messages.info(request, 'Login Success')
                return redirect('homepage')
            else:
                return redirect('/')
        else:
            messages.info(request, 'Invalid username/password')

    return render(request, 'website/login.html')


######################## Logout Views ##########################
def Logout_view(request):
    logout(request)
    return redirect('login')


def GetUsername(request):
    if request.method == "POST":
        username = request.POST.get("username")

    if User.objects.filter(username=username).exists():
        amount = "Username is already Taken"
        return JsonResponse({'amount' : amount}, status=200)

    else:
        amount = ""
        return JsonResponse({'amount' : amount}, status=200)


def GetEmail(request):
    if request.method == "POST":
        email = request.POST.get("email")

    if User.objects.filter(email=email).exists():
        amount = "Email is already Taken"
        return JsonResponse({'amount' : amount}, status=200)

    else:
        amount = ""
        return JsonResponse({'amount' : amount}, status=200)
