from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Patient, Prescription

# Unregister the Group and User models
admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nhs_number', 'first_name', 'last_name', 'date_of_birth')
    search_fields = ('nhs_number', 'first_name', 'last_name')
    list_filter = ('created_at',)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('reference_number', 'patient', 'medication_name', 'dosage')
    search_fields = ('reference_number', 'medication_name', 'patient__first_name', 'patient__last_name')
    list_filter = ('created_at',)

# Customize the admin site header and title
admin.site.site_header = 'Hospital Management System'
admin.site.site_title = 'Hospital Management'
admin.site.index_title = 'Hospital Management Dashboard'
