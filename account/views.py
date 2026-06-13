from django.shortcuts import render , redirect
from django.contrib.auth.forms import  UserCreationForm 
from .models import User , UserManager
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UserCreateForm
from django.contrib.auth import login , authenticate 


from doing.models import Planer
# Create your views here.


def SignupView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/login/')
        else:
            messages.add_message(request,messages.ERROR,'invalid values')

    return render(request,'account/signup.html')
        



def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if '@' in username:
            try:
                username=(User.objects.get(email=username).username).lower().strip()
            except user.DoseNotExist:
                messages.add_message(request,messages.ERROR,'username or password is incorrect')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'username or password is incorrect')

    return render(request,'account/login.html')
   
