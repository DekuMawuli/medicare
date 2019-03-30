from django.db import models

# Create your models here.

class Doctor_SignUp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    doctor_license = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    Date_of_Birth = models.DateField()
    email = models.EmailField()
    doc_pass = models.CharField(max_length=20)


    def __str__(self):
        return 'Dr. ' + self.first_name


class Nurse_SignUp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    nurse_license = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    Date_of_Birth = models.DateField()
    email = models.EmailField()
    nurse_pass = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Patient_SignUp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    Date_of_Birth = models.DateField()
    email = models.EmailField()
    patient_pass = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name

