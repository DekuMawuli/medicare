
from django.shortcuts import render, redirect
from .forms import Register_Doctor, Register_Patient, Register_Nurse, Login_Doc,Login_Nurse,Login_Patient
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    form = Register_Doctor()
    if request.method == "POST":
        form = Register_Doctor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor-profile')
    return render(request, 'startUp/home.html', {'form': form})


def home_patient(request):
    form = Register_Patient()
    if request.method == "POST":
        form = Register_Patient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-profile')
    return render(request, 'startUp/patient_signUp.html', {'form': form})


def home_nurse(request):
    form = Register_Nurse()
    if request.method == "POST":
        form = Register_Nurse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nurse-profile')
    return render(request, 'startUp/nurse_signUp.html', {'form': form})




@login_required()
def doctor_home(request):
    return render(request, 'startUp/doctorSignIn.html')

@login_required()
def nurse_home(request):
    return render(request, 'startUp/nurse_sigIn.html')

@login_required()
def patient_home(request):
    return render(request, 'startUp/patient SignIn.html')