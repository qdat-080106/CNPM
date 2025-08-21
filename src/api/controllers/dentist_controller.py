from flask import Blueprint, request, jsonify
from services.dentist_service import DentistService
from services.appointment_service import AppointmentService
from infrastructure.repositories.dentist_repository import DentistRepository
from infrastructure.repositories.appointment_repository import AppointmentRepository
from api.schemas.dentist import DentistResponseSchema, AvailabilitySchema
from api.schemas.appointment import AppointmentRequestSchema, AppointmentResponseSchema, AppointmentResultSchema

bp_dentist = Blueprint('dentist', __name__, url_prefix='/dentists')
bp_appointment = Blueprint('appointment', __name__, url_prefix='/appointments')

dentist_service = DentistService(DentistRepository())
appointment_service = AppointmentService(AppointmentRepository())
dentist_response_schema = DentistResponseSchema()
availability_schema = AvailabilitySchema()
appointment_request_schema = AppointmentRequestSchema()
appointment_response_schema = AppointmentResponseSchema()
appointment_result_schema = AppointmentResultSchema()

@bp_dentist.route('/', methods=['GET'])
def list_dentists():
    dentists = dentist_service.list_all_dentists()
    return jsonify(dentist_response_schema.dump(dentists, many=True)), 200

@bp_dentist.route('/<int:dentist_id>/availability', methods=['POST'])
def set_dentist_availability(dentist_id):
    data = request.get_json()
    errors = availability_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    updated_dentist = dentist_service.update_availability(dentist_id, data)
    return jsonify(dentist_response_schema.dump(updated_dentist)), 200

@bp_appointment.route('/', methods=['POST'])
def create_appointment():
    data = request.get_json()
    errors = appointment_request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_appointment = appointment_service.create_appointment(data)
    return jsonify(appointment_response_schema.dump(new_appointment)), 201

@bp_appointment.route('/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    data = request.get_json()
    errors = appointment_request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    updated_appointment = appointment_service.update_appointment(appointment_id, data)
    return jsonify(appointment_response_schema.dump(updated_appointment)), 200

@bp_appointment.route('/<int:appointment_id>/result', methods=['PUT'])
def update_appointment_result(appointment_id):
    data = request.get_json()
    errors = appointment_result_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    updated_appointment = appointment_service.update_result(appointment_id, data)
    return jsonify(appointment_response_schema.dump(updated_appointment)), 200