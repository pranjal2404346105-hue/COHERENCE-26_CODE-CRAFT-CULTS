from django.shortcuts import render
from .models import Patient, ClinicalTrial
from .matcher import calculate_match


def patient_list(request):

    patients = Patient.objects.all()

    return render(request,"patients.html",{"patients":patients})


def patient_trials(request, patient_id):

    patient = Patient.objects.get(patient_id=patient_id)

    trials = ClinicalTrial.objects.all()

    matches = []

    for trial in trials:

        score,reasons = calculate_match(patient,trial)

        matches.append({
            "trial":trial,
            "score":score,
            "reasons":reasons
        })

    matches.sort(key=lambda x: x["score"], reverse=True)

    return render(request,"dashboard.html",{
        "patient":patient,
        "matches":matches
    })
