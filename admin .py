from django.contrib import admin
from .models import Patient, LabResult, ClinicalTrial, User

admin.site.register(Patient)
admin.site.register(LabResult)
admin.site.register(ClinicalTrial)
admin.site.register(User)
