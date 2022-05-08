from django.urls import path
from hospital.models import Patient
from . import views
app_name = "hospital"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.patient_registration, name='register'),
    path('login/', views.login_request, name='login'),
    path('patients/', views.all_patients, name='patients'),
    path('doctordashboard/', views.doctor_dashboard, name='patients')
    
]