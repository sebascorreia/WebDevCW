from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View, generic
from .forms import UserRegForm, PatientRegForm, AppointmentForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Patient, Doctor, Appointment
from django.forms import ModelForm
from django.http import HttpResponse

def index(request):     
    current_user = request.user
    doctor = ''
    if request.user.is_authenticated:
        if Doctor.objects.filter(user=current_user).exists():
            doctor = Doctor.objects.filter(user=current_user)
    return render(request, 'hospital/index.html', {'doctor': doctor})


def doctor_dashboard(request):
    return render(request, 'hospital/doctor_dashboard.html')

def logout_view(request):
    logout(request)
    return render(request, 'hospital/index.html')

def patient_dashboard(request):
    return render(request, 'hospital/patient_dashboard.html')

def patappointment_click(request):
    return render(request, 'hospital/patappointments_click.html')
def docappointment_click(request):
    return render(request, 'hospital/docappointements_click.html')

def all_patients(request):
    current_user = request.user
    doctor = ''
    if request.user.is_authenticated:
        if Doctor.objects.filter(user=current_user).exists():
            doctor = Doctor.objects.filter(user=current_user)
        patient_list = Patient.objects.all()
        return render(request, 'hospital/patient_list.html', {'doctor': doctor, 'patient_list': patient_list})
    else:
        messages.info("ACCESS DENIED")
        return redirect("hospital:login")

def appointmentdetail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'hospital/appointment_detail.html', {'appointment': appointment})

def allappointments(request):
    current_user = request.user
    if Doctor.objects.filter(user=current_user).exists():
        appointment_list = Appointment.objects.all()
        return render(request, 'hospital/appointment_list.html',
                      {'appointment_list': appointment_list})
    else:
        messages.info("ACCESS DENIED")
        return redirect("hospital:login")

def unassigned_appointments(request):
    current_user = request.user
    if Doctor.objects.filter(user= current_user).exists():
        appointment_list = Appointment.objects.filter(doctorId__isnull =True)
        return render(request, 'hospital/appointment_list.html',
                      {'appointment_list': appointment_list})
    else:
        messages.info("ACCESS DENIED")
        return redirect("hospital:login")
def myappointments(request):
    current_user = request.user
    if Patient.objects.filter(user = current_user).exists():
        patient = Patient.objects.get(user = current_user)
        appointment_list = Appointment.objects.filter(patientId = patient)
    elif Doctor.objects.filter(user= current_user).exists():
        doctor = Doctor.objects.get(user = current_user)
        appointment_list = Appointment.objects.filter(doctorId=doctor)
    else:
        messages.info("Please login or signup")
        return redirect("hospital:login")
    return render(request, 'hospital/appointment_list.html',
                  {'appointment_list': appointment_list})

class AppointmentUpdate(generic.UpdateView):
    model = Appointment
    template_name= 'hospital/appointment_edit.html'
    def get_form_class(self):
        if Doctor.objects.filter(user=self.request.user).exists():
            return AppointmentUpdate_doc
        elif Patient.objects.filter(user=self.request.user).exists():
            return AppointmentUpdate_pat


class AppointmentUpdate_doc(ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctorId', 'appointmentDate', 'department','status']



class AppointmentUpdate_pat(ModelForm):
    class Meta:
        model = Appointment
        fields = ['description', 'department']

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
                if Patient.objects.filter(user=user).exists():
                    return redirect("hospital:patientdashboard")
                elif Doctor.objects.filter(user=user).exists():
                    return redirect("hospital:doctordashboard")
            else:
                messages.error(request, "Invalid email or password.")
                #return HttpResponse(status=401)
        else:
            messages.error(request, "Invalid email or password.")
            #return HttpResponse(status=401)
            
    form = AuthenticationForm()
    return render(request = request, template_name="hospital/login.html",context = {"login_form":form})

def appointment_view(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        current_user = request.user
        if current_user.is_authenticated:
            patientID = Patient.objects.get(user=current_user)
            if patientID is not None and form.is_valid():
                appointment =form.save(commit = False)
                appointment.patientId= patientID
                if patientID.assignedDoctorId is not None:
                    appointment.doctorId = patientID.assignedDoctorId
                appointment.save()
                return redirect("hospital:index")
            else:
                messages.info(request, 'invalid registration details')
                return render(
                    request,
                    "appointment.html",
                    {"form": form}  # This still includes the errors instead of creating a new form
                )
        else:
            messages.info("Please login or signup")
            return redirect("hospital:login")
    form = AppointmentForm()
    return render(request=request, template_name="hospital/appointment.html", context={"form": form})

