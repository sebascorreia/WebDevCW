from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hospital.views import index, doctor_dashboard, patient_dashboard, all_patients, patient_registration, login_request, appointment_view, allappointments, myappointments, unassigned_appointments, appointmentdetail, AppointmentUpdate
from hospital.models import Doctor, Patient, Appointment, Bill, User
from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth import get_user_model



# Create your tests here.
class TestUrls(SimpleTestCase):
            

    def test_index_url_is_resolved(self):
        url = reverse('hospital:index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_register_url_is_resolved(self):
        url = reverse('hospital:register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, patient_registration)

    def test_login_url_is_resolved(self):
        url = reverse('hospital:login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_request)

    def test_patients_url_is_resolved(self):
        url = reverse('hospital:patients')
        client = Client()    
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_patients)


    def test_doctordashboard_url_is_resolved(self):
        url = reverse('hospital:doctordashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_dashboard)

    def test_patientdashboard_url_is_resolved(self):
        url = reverse('hospital:patientdashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, patient_dashboard)

    def test_request_appointment_url_is_resolved(self):
        url = reverse('hospital:request_appointment')
        print(resolve(url))
        self.assertEquals(resolve(url).func, appointment_view)

    def test_allappointments_url_is_resolved(self):
        url = reverse('hospital:appointment_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, allappointments)

    def test_myappointments_url_is_resolved(self):
        url = reverse('hospital:myappointments')
        print(resolve(url))
        self.assertEquals(resolve(url).func, myappointments)

    def test_unassigned_appointments_url_is_resolved(self):
        url = reverse('hospital:unassigned_appointments')
        print(resolve(url))
        self.assertEquals(resolve(url).func, unassigned_appointments)

    def test_appointmentdetail_url_is_resolved(self):
        url = reverse('hospital:appointment_detail', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func, appointmentdetail)

    def test_appointment_edit_url_is_resolved(self):
        url = reverse('hospital:appointment_edit', args=[3])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AppointmentUpdate)

