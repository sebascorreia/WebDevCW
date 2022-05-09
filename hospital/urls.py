from django.urls import path
from hospital.models import Patient
from . import views
app_name = "hospital"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.patient_registration, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('patients/', views.all_patients, name='patients'),
    path('doctordashboard/', views.doctor_dashboard, name='doctordashboard'),
    path('patientdashboard/', views.patient_dashboard, name='patientdashboard'),
    path('request_appointment/', views.appointment_view,name = 'request_appointment'),
    path('allappointments/', views.allappointments, name='appointment_list'),
    path('myappointments/', views.myappointments, name='myappointments'),
    path('unassigned_appointments', views.unassigned_appointments, name='unassigned_appointments'),
    path('appointment_detail/<int:appointment_id>', views.appointmentdetail, name='appointment_detail'),
    path('appointment_edit/<int:pk>', views.AppointmentUpdate.as_view(), name='appointment_edit'),
    path('appointments_pat', views.patappointment_click, name='patappointments' ),
    path('appointments_doc', views.docappointment_click, name='docappointments' ),
]