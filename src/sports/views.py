from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            first_name = userObj['first_name']
            last_name = userObj['last_name']
            if not (User.objects.filter(username=username).exists()) or User.objects.filter(email=email).exists():
                user = User.objects.create_user(username, email, password)
                user.last_name = last_name
                user.first_name = first_name
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like that username or email already exists')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form' : form})
