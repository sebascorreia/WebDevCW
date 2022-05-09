from http import client
from django.test import TestCase


from django.test import TestCase, Client
from django.urls import reverse, resolve
from hospital.models import Doctor, Patient, Appointment, Bill
from django.contrib.auth.models import User
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

    #def test_index_GET(self):
        
        # user, client = self.login()
        # response = self.client.get(self.index_url)
        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'hospital/index.html')

    # def test_doctor_dashboard_GET(self):
    #     response = self.client.get(self.doctordashboard_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hospital/doctor_dashboard.html')

    # def test_patient_dashboard_dashboard_GET(self):
    #     response = self.client.get(self.patientdashboard_url)

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'hospital/patient_dashboard.html')

    # def test_register_GET(self):
    #     response = self.client.get(self.register_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hospital/patient_signup.html')

    # def test_login_GET(self):
    #     response = self.client.get(self.login_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hospital/login.html')

    # def test_patient_list_GET(self):
    #     response = self.client.get(self.patientlist_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'hospital/patient_list.html')


