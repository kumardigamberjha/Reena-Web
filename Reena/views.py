from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from website.forms import CreateUserForm

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Reena import settings

from datetime import date



######################## SignUp Views ##########################
def Signup_view(request):
    form = CreateUserForm()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for "+ user+ " succesfully")
            return redirect('login')

    return render(request, 'website/Signup.html', {'form':form})

######################## Login Views ##########################

def Login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = username
            # return redirect('/')
            if user.is_superuser:
                messages.info(request, 'Login Success')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('homepage')
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            else:
                messages.info(request, 'Login Success')
                return redirect('homepage')
        else:
            messages.info(request, 'Invalid username/password')

    return render(request, 'website/login.html')


######################## Logout Views ##########################
@login_required
def Logout_view(request):
    logout(request)
    return redirect('login')

