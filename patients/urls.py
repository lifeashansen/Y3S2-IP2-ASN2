from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_patient, name='register_patient'),
    path('patients/', views.patient_list, name='patient_list'),
]
