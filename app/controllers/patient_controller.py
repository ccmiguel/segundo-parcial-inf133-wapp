from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.patient_model import Patient
from views import patient_view

# Importamos el decorador de roles
from utils.decorators import role_required

patient_bp = Blueprint("patient", __name__)

@patient_bp.route("/patients")
@login_required
def list_patients():
    patients = Patient.get_all()
    return patient_view.list_patients(patients)


@patient_bp.route("/patients/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_patient():
    if request.method == "POST":
        if current_user.has_role("admin"):
            id = int(request.form["id"])
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birth_day = request.form["birth_day"]
            patient = Patient(id=id, name=name, lastname=lastname, ci=ci, birth_day=birth_day)
            patient.save()
            flash("Patient creado exitosamente", "success")
            return redirect(url_for("patient.list_patients"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return patient_view.create_patient()

@patient_bp.route("/patients/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_patient(id):
    patient = Patient.get_by_id(id)
    if not patient:
        return "Patient no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birth_day = request.form["birth_day"]
            patient.update(name=name, lastname=lastname, ci=ci, birth_day=birth_day)
            flash("Patient actualizado exitosamente", "success")
            return redirect(url_for("patient.list_patients"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return patient_view.update_patient(patient)

@patient_bp.route("/patients/<int:id>/delete")
@login_required
@role_required("admin")
def delete_patient(id):
    patient = Patient.get_by_id(id)
    if not patient:
        return "Patient no encontrado", 404
    if current_user.has_role("admin"):
        patient.delete()
        flash("Patient eliminado exitosamente", "success")
        return redirect(url_for("patient.list_patients"))
    else:
        return jsonify({"message": "Unauthorized"}), 403

