from flask import Blueprint, request, jsonify
from services.clinic_service import ClinicService
from infrastructure.repositories.clinic_repository import ClinicRepository
from api.schemas.clinic import ClinicRequestSchema, ClinicResponseSchema, ServiceRequestSchema, ServiceResponseSchema

bp = Blueprint('clinic', __name__, url_prefix='/clinics')

clinic_service = ClinicService(ClinicRepository())
clinic_request_schema = ClinicRequestSchema()
clinic_response_schema = ClinicResponseSchema()
service_request_schema = ServiceRequestSchema()
service_response_schema = ServiceResponseSchema()

@bp.route('/', methods=['GET'])
def list_clinics():
    clinics = clinic_service.list_all_clinics()
    return jsonify(clinic_response_schema.dump(clinics, many=True)), 200

@bp.route('/', methods=['POST'])
def create_clinic():
    data = request.get_json()
    errors = clinic_request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_clinic = clinic_service.create_clinic(data)
    return jsonify(clinic_response_schema.dump(new_clinic)), 201

@bp.route('/<int:clinic_id>/services', methods=['GET'])
def list_services_by_clinic(clinic_id):
    services = clinic_service.get_services_by_clinic(clinic_id)
    return jsonify(service_response_schema.dump(services, many=True)), 200

@bp.route('/services', methods=['POST'])
def create_service():
    data = request.get_json()
    errors = service_request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_service = clinic_service.create_service(data)
    return jsonify(service_response_schema.dump(new_service)), 201