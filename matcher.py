def calculate_match(patient, trial):

    score = 0
    reasons = []

    if trial.disease.lower() in patient.diagnosis.lower():
        score += 50
        reasons.append("Disease matches trial")

    if "hb" in trial.inclusion_criteria.lower():
        score += 20
        reasons.append("Lab criteria satisfied")

    if patient.medications.lower() in trial.exclusion_criteria.lower():
        score -= 20
        reasons.append("Medication conflict")

    return score, reasons
