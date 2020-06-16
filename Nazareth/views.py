from django.shortcuts import render,redirect
from . forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Profile,Appointments
import datetime as dt
# Create your views here.


def index(request):
    loginTime(request)  
    return render(request,"index.html",{})

@login_required(login_url='/admin/login')
def patients(request):
    loginTime(request)
    patients = Profile.objects.filter(role="patient")
    return render(request,"patients.html",{"patients":patients})

@login_required(login_url='/admin/login')
def doctors(request):
    loginTime(request)
    doctors = Profile.objects.filter(role="doctor")
    return render(request,"doctors.html",{"doctors":doctors})

@login_required(login_url='/admin/login')
def nurses(request):
    loginTime(request)
    nurses = Profile.objects.filter(role="nurse")
    return render(request,"nurses.html",{"nurses":nurses})

@login_required(login_url='/admin/login')
def technicians(request):
    loginTime(request)
    technicians = Profile.objects.filter(role="technician")
    return render(request,"technicians.html",{"technicians":technicians})

@login_required(login_url='/admin/login')
def appointment(request):
    loginTime(request)
    appointments = Appointments.objects.all()
    return render(request,"appointment.html",{"appointments":appointments})

@login_required(login_url='/admin/login')
def search_results(request):
    loginTime(request)
    if 'user' in request.GET or request.GET['user']:
        search_item = request.GET.get('user')
        searched_users = Profile.objects.filter(email=search_item)
        return render(request, 'search.html',{"users": searched_users})
    else:
        return redirect("/")

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,email=email, password=raw_password)
            profile = Profile(user=user)
            profile.save()
            user.is_active = True
            login(request,user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'sign.html', {'form': form})


def loginTime(request):
     if request.user:
        profile = Profile.objects.get(user=request.user)
        profile.last_login = dt.datetime.now()
        profile.save()
    