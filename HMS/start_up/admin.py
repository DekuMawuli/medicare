from django.contrib import admin
from .models import Doctor_SignUp, Patient_SignUp, Nurse_SignUp
# Register your models here.

admin.site.register(Doctor_SignUp)
admin.site.register(Nurse_SignUp)
admin.site.register(Patient_SignUp)