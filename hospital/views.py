from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import UserRegForm, PatientRegForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Patient

def index(request):
    return render(request, 'hospital/index.html')


def doctor_dashboard(request):
    return render(request, 'hospital/doctor_dashboard.html')

def all_patients(request):
    patient_list = Patient.objects.all()
    return render(request, 'hospital/patient_list.html',
        {'patient_list': patient_list})


def patient_registration(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        patient_form = PatientRegForm(request.POST)
        if form.is_valid() and patient_form.is_valid():
            user = form.save()

            patient = patient_form.save(commit = False)
            patient.user = user
            patient.save()
            login(request,user)
            messages.success(request, "Registration successful.")
            return redirect("hospital:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegForm()
        patient_form = PatientRegForm()
    context = {'form': form, 'patient_form' : patient_form }
    return render (request= request, template_name="hospital/patient_signup.html", context= context)

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user=authenticate(username=username, password= password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {user.first_name}.")
                return redirect("hospital:index")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(request = request, template_name="hospital/login.html",context = {"login_form":form})