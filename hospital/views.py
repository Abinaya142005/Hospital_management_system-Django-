from django.shortcuts import render
from .models import Patient, Prescription

def home(request):
    num_patients = Patient.objects.count()
    num_prescriptions = Prescription.objects.count()
    
    context = {
        'num_patients': num_patients,
        'num_prescriptions': num_prescriptions,
        'title': 'Hospital Management System'
    }
    return render(request, 'hospital/home.html', context)
