from django.test import TestCase
from hospital.models import Doctor, Patient, Appointment, User

class TestModels(TestCase):

    def setUp(self):
        self.doctor1 = Doctor.objects.create(
            user=User(),
            address='35 doctor street',
            phone='07572316693',
            department='cardiology',
            image='image/image.png'

        )

    