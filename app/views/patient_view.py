from flask import render_template
from flask_login import current_user


# La función `list_animals` recibe una lista de
# animales y renderiza el template `animales.html`
def list_patients(patients):
    return render_template(
        "patients.html",
        patients=patients,
        title="Lista de Patients",
        current_user=current_user,
    )


# La función `create_animal` renderiza el
# template `create_animal.html` o devuelve un JSON
# según la solicitud
def create_patient():
    return render_template(
        "create_patients.html", title="Crear Patients", current_user=current_user
    )


# La función `update_animal` recibe un animal
# y renderiza el template `update_animal.html`
def update_patient(patient):
    return render_template(
        "update_patient.html",
        title="Editar Patient",
        patient=patient,
        current_user=current_user,
    )