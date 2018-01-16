from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import redirect
from .forms import UserRegistrationForm
import praw
import pdb

# Create your views here.

def index(request):
    reddit = praw.Reddit(client_id='O0r4WVJ1VWL7TA',
                     client_secret='8oVSvH15EVK-2hQ5T5ljDcghXKI',
                     refresh_token='49102260-Bpjg-Kx0yljN_qZSGKlzRR-6RHo',
                     user_agent='sickplays')


    posts = []

    for submission in reddit.subreddit('soccer+nba+nfl').hot(limit=150):
        if submission.media is not None:
            if submission.domain == 'streamable.com':
                posts.append([submission.url[:23] + 't/' + submission.url[23:], submission.title])
            if submission.domain == 'clippituser.tv':
                posts.append([submission.url[:29] + 'embed_iframe/' + submission.url[29:], submission.title])
    return render(request, 'index.html', { 'posts' : posts})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
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
