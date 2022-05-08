from http import client
from django.test import TestCase


from django.test import TestCase, Client
from django.urls import reverse
from hospital.models import Doctor, Patient, Appointment, Bill
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('hospital:index')
        self.doctordashboard_url = reverse('hospital:doctordashboard')
        self.patientdashboard_url = reverse('hospital:patientdashboard')
        self.register_url = reverse('hospital:register')
        self.login_url = reverse('hospital:login')
        self.patientlist_url = reverse('hospital:patients')

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/index.html')

    def test_doctor_dashboard_GET(self):
        response = self.client.get(self.doctordashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/doctor_dashboard.html')

    def test_patient_dashboard_dashboard_GET(self):
        response = self.client.get(self.patientdashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/patient_dashboard.html')

    def test_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/patient_signup.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/login.html')

    def test_patient_list_GET(self):
        response = self.client.get(self.patientlist_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/patient_list.html')
