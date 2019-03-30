from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('patient', views.home_patient, name='home-patient'),
    path('nurse', views.home_nurse, name='home-nurse'),
    path('doctor-home', views.doctor_home, name='doctor-page'),
    path('nurse-home', views.nurse_home, name='nurse-page'),
    path('patient-home', views.patient_home, name='patient-page'),
    path('nurse-login', LoginView.as_view(template_name='startUp/nurse_sigIn.html'), name='nurse-login'),
    path('patient-login', LoginView.as_view(template_name='startUp/patient SignIn.html'), name='patient-login'),
    path('doctor-login', LoginView.as_view(template_name='startUp/doctorSignIn.html'), name='doctor-login'),
    path('prodile/doctor-profile', LoginView.as_view(template_name='profile/doctor-profile.html'), name='doctor-profile'),
    path('profile/nurse-profile', LoginView.as_view(template_name='profile/nurse-profile.html'), name='nurse-profile'),
    path('profile/patient-profile', LoginView.as_view(template_name='profile/patient-profile.html'), name='patient-profile'),
]
