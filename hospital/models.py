from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
('Other','Other')
]
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40, null = True)
    phone = PhoneNumberField(null =True, blank = False, unique = True, default='1234567890')
    department = models.CharField(max_length=50, null = False, choices = departments,default='Cardiologist')
    image = models.ImageField(upload_to='hospital/static/hospital/profile_pics', null = True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.department + ")"
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40,null=True)
    phone = PhoneNumberField(null=True)
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
    appointmentDate = models.DateField(null = True)
    description = models.TextField(max_length=1000)
    status = models.BooleanField(default=False)
    subject = models.TextField(max_length=50, null = False)
    department = models.CharField(max_length=50, choices=departments, null=True)
    date_created = models.DateField(auto_now=True)
class Bill(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    otherCharges = models.PositiveIntegerField(null=False)

