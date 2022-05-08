from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hospital.views import index, doctor_dashboard, patient_dashboard, all_patients, patient_registration, login_request

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
