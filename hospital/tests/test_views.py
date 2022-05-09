from http import client
from django.test import TestCase


from django.test import TestCase, Client
from django.urls import reverse, resolve
from hospital.models import Doctor, Patient, Appointment, Bill
from django.contrib.auth.models import User
from django.contrib import auth, create_user
import json

class TestViews(TestCase):

    def login(self):
        self.username = 'test1'
        self.password = '12345qwe'
        user = User.objects.create_user(username=self.username)
        user.set_password(self.password)
        client = Client()
        client.login(username=self.username, password=self.password)
        return user, client

    def setUp(self):
        self.index_url = reverse('hospital:index')
        self.doctordashboard_url = reverse('hospital:doctordashboard')
        self.patientdashboard_url = reverse('hospital:patientdashboard')
        self.register_url = reverse('hospital:register')
        self.patientlist_url = reverse('hospital:patients')
        self.login_url = reverse('hospital:login')
        return super().setUp()

    def test_index_GET(self):
        
        user, client = self.login()
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

    def test_that_user_gets_logged_in(self):
        user, client = self.login()
        self.assertIn(user.id, self.client.session)


    # def test_patient_list_GET(self):
    #     d = Doctor()

    #     my_user = User.objects.create()
    #     d.user = my_user


    #     response = self.client.get(self.patientlist_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hospital/patient_list.html')


