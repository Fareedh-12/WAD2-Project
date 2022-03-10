from django.shortcuts import render
from django.http import HttpResponse
from radar.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



def homepage1(request):
    return render(request, 'radar/homepage1.html')

@login_required
def homepage2(request):
    return render(request, 'radar/homepage2.html')

@login_required
def friendspage(request):
    return render(request, 'radar/friendspage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(username=username, password=password)
    
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('radar:homepage2'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, "radar/login.html")


def signup(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'radar/signup.html', context = {'user_form': user_form,
                                                            'profile_form':profile_form,
                                                            'registered': registered})

@login_required
def account(request):
    return render(request, 'radar/account.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('radar:homepage1'))
