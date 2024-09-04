from django.shortcuts import render

from .models import User 
from . import forms
from .forms import UserInfo, UserProfileInfoForm

#import for login functionality (httpresponseredirect also included for this)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


#login view 
def user_login(request):
    
    if request.method =='post':
        username = request.POST.get('username') #in html form we put the name ='username' in input tag
        password = request.POST.get('password') #same as above
        
        user = authenticate(username = username, password = password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse(reverse('app2:test'))#if they are login and their account is active go to this page
            else:
                return HttpResponse('Account is not active!')
        
        else:
            return HttpResponse('login authentication failed!')
            print(f'username: {username}, \nPassword: {password}')
    else: #if request method is not post
        return render(request, 'app2/login.html')

#logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('test'))



def home(request):
    return render(request, 'app2/home.html')

def users_page(request):
    users = User.objects.all()
    list = {'users_list': users}
    return render(request, 'app2/users.html', context= list)


#level 5 practice usermodels

def launching_page(request):
    registered = False
    if request.method == 'POST':
        user_form = UserInfo(data = request.POST)
        user_profile = UserProfileInfoForm(data = request.POST)
        
        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = user_profile.save(commit=False)
            profile.user = user
            
            #if image is uploaded
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
                print(user_form.errors, user_profile.errors)
    else:
        user_form = UserInfo()
        user_profile = UserProfileInfoForm()
        
        
    return render(request, 'app2/launching_soon.html', context={'registered': registered, 'user_form': user_form, 'user_profile': user_profile})


def contact_page(request):
    form = forms.info_form()
    
    if request.method == 'POST':
        form = forms.info_form(request='POST')  
        
    #to validate the form is working correctly
    if form.is_valid():
        print('validation successful')
        print("Name: " + form.cleaned_data['name'])
        print("email: " + form.cleaned_data['email'])
        print("Bio: " + form.cleaned_data['bio'])
    
    forms_list = {'form': form}
    return render(request, 'app2/contact_info.html', context = forms_list)

@login_required
def test(request):
    return HttpResponse('<h1>This is Test page<h1>')


