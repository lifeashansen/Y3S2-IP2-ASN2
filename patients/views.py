from django.shortcuts import render, redirect

# Create your views here.
from .forms import PatientForm
from .models import Patient

def home(request):
    return render(request, 'home.html')

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'register.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all().order_by('-date_registered')
    return render(request, 'patient_list.html', {'patients': patients})
