from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required



def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register/index.html', {'form': form})


def homepage(request):
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        #if form.is_valid():
         #   form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            user = authenticate(request.POST)
            if user is not None:
                login(request, user)
                return redirect('user_dashboard')
   #     form = SignUpForm()
    return render(request, 'register/homepage.html', {})


@login_required()
def user_dashboard(request):
    return render(request, 'register/dashboard.html', {})
