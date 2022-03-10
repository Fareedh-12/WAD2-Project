from django.shortcuts import render
from django.http import HttpResponse
from radar.forms import UserForm, UserProfileForm
from radar.models import UserProfile, FriendList, Session


def homepage(request):
    return render(request, 'radar/homepage.html')


def friendspage(request):
    return render(request, 'radar/friendspage.html')


def login(request):
    return render(request, 'radar/login.html')


def signup(request):
    return render(request, 'radar/signup.html')


def account(request):
    return render(request, 'radar/account.html')
