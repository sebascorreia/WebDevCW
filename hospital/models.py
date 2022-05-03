from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40, null = True)
    phone = PhoneNumberField(null =True, blank = False, unique = True, default='1234567890')
    department = models.CharField(max_length=20, null = False)
    image = models.ImageField(upload_to='hospital/static/hospital/profile_pics', null = True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.department+ ")"
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40,null=True)
    phone = PhoneNumberField(null=True, blank=False, unique=False, default='1234567890')
    image = models.ImageField(upload_to='hospital/static/hospital/profile_pics',null= True)
    description = models.CharField(max_length=500,null=True)
    assignedDoctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    admitDate = models.DateField(null=True)
    admitStatus = models.BooleanField(default=False)




    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Appointment(models.Model):
    patientId = models.ForeignKey(Patient, on_delete= models.CASCADE)
    doctorId = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

class Bill(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    otherCharges = models.PositiveIntegerField(null=False)

