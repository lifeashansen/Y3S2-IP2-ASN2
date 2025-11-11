from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'gender', 'phone', 'date_registered')
    search_fields = ('full_name', 'phone')
    list_filter = ('gender',)


admin.site.register(Patient, PatientAdmin)

