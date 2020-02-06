from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone


def index(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username is taken already')
            elif User.objects.filter(email=email).exists():
                print('Email is alreagy taken')
            else:
                user = User.objects.create_user(username=username, 
                first_name=first_name, 
                last_name=last_name, 
                email=email,
                password=password1)
                user.save()
        else:
            print('Paswords not maching')
        return HttpResponseRedirect(reverse('accounts:index'))
    else:
        return render(request, 'accounts/register.html')

#def login(request):
#   return render()