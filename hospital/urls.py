from django.urls import path

from . import views
app_name = "hospital"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.patient_registration, name='register'),
    path('login/', views.login_request, name='login'),
]