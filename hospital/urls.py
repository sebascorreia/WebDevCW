from django.urls import path
from hospital.models import Patient
from . import views
app_name = "hospital"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.patient_registration, name='register'),
    path('login/', views.login_request, name='login'),
    path('patients/', views.all_patients, name='patients'),
    path('doctordashboard/', views.doctor_dashboard, name='doctordashboard'),
    path('patientdashboard/', views.patient_dashboard, name='patientdashboard'),
    path('request_appointment/', views.appointment_view,name = 'request_appointment'),
    path('allappointments/', views.allappointments, name='appointment_list'),
    path('myappointments/', views.myappointments, name='myappointments'),
    path('unassigned_appointments', views.unassigned_appointments, name='unassigned_appointments')

]