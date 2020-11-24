from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
from django.conf.urls.static import static
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
from annoying.decorators import ajax_request

from django.core.mail import send_mail
'''
send mail enables sends confirmation mail using @gmail
'''
from django.contrib.auth.decorators import login_required
'''
The @login_required declarator limits access of view function to only
authenticated users
'''
# Create your views here.

#Home page view function
@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    all_users = Profile.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'display/home.html',  {"all_images": all_images}, {"all_users":all_users})

#Explore page view function
@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'display/explore.html')

#Notification page view function
@login_required(login_url='/accounts/login/')
def notification(request):
    return render(request, 'display/notification.html')

#Profile page view function
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'display/userprofile.html')

#Log-Out page view function
def logout(request):
    return render(request, 'registration/logout.html')

#Login page view function
def login(request):
    return render(request, 'registration/login.html')

#Login page view function
@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.imageuploader_profile= p
            post.save()
            return redirect('/')
    else:
        form =PostForm
    return render(request, 'display/upload.html', {"form": form})

#Like view function

