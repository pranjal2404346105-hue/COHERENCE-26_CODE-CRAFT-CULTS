from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):

    ROLE_CHOICES = (
        ('doctor','Doctor'),
        ('researcher','Researcher'),
        ('crc','Clinical Research Coordinator'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)



class Patient(models.Model):

    patient_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    age = models.IntegerField()

    gender = models.CharField(max_length=10)

    diagnosis = models.TextField()

    medications = models.TextField()

    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.patient_id)



class LabResult(models.Model):

    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

    test_name = models.CharField(max_length=100)

    value = models.FloatField()

    date = models.DateField()



class ClinicalTrial(models.Model):

    title = models.CharField(max_length=200)

    phase = models.CharField(max_length=20)

    disease = models.CharField(max_length=200)

    inclusion_criteria = models.TextField()

    exclusion_criteria = models.TextField()

    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
