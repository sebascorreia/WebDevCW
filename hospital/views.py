from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import UserRegForm, PatientRegForm
from django.contrib import messages

def index(request):
    return render(request, 'hospital/index.html')

def patient_registration(request):
    if request.method == "POST":
        form =UserRegForm(request.POST)
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