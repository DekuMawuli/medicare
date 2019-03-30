from django import forms
from .models import Doctor_SignUp, Nurse_SignUp, Patient_SignUp

class Register_Doctor(forms.ModelForm):
    class Meta:
        model = Doctor_SignUp
        fields = [
            'first_name', 'last_name', 'doctor_license', 'email', 'Date_of_Birth', 'hospital', 'phone_number', 'region', 'doc_pass'
        ]


class Register_Patient(forms.ModelForm):
    class Meta:
        model = Patient_SignUp
        fields = [
            'first_name', 'last_name', 'email', 'Date_of_Birth', 'hospital' , 'phone_number', 'region', 'patient_pass'
        ]


class Register_Nurse(forms.ModelForm):
    class Meta:
        model = Nurse_SignUp
        fields = [
            'first_name', 'last_name', 'email', 'Date_of_Birth', 'hospital', 'nurse_license', 'phone_number', 'region', 'nurse_pass'
        ]



class Login_Nurse(forms.ModelForm):
    class Meta:
        model = Nurse_SignUp
        fields = [
            'email', 'nurse_pass'
            ]

class Login_Doc(forms.ModelForm):
    class Meta:
        model = Doctor_SignUp
        fields = [
            'email', 'doc_pass'
            ]
class Login_Patient(forms.ModelForm):
    class Meta:
        model = Patient_SignUp
        fields = [
            'email', 'patient_pass'
            ]