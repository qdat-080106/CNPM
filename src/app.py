from flask import Flask
from flasgger import Swagger
from config import config_by_name
from infrastructure.databases import db

# Import tất cả các SQLAlchemy models để chúng được tạo bảng
from infrastructure.models.user_model import UserModel
from infrastructure.models.clinic_model import ClinicModel
from infrastructure.models.dentist_model import DentistModel
from infrastructure.models.appointment_model import AppointmentModel
from infrastructure.models.chat_model import ConversationModel, MessageModel
from infrastructure.models.todo_model import TodoModel

# Import và đăng ký tất cả các Blueprint (Controllers)
from api.controllers.auth_controller import bp as auth_bp
from api.controllers.clinic_controller import bp as clinic_bp
from api.controllers.dentist_controller import bp_dentist as dentist_bp
from api.controllers.dentist_controller import bp_appointment as appointment_bp
from api.controllers.chat_controller import bp as chat_bp
from api.controllers.todo_controller import bp as todo_bp

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Khởi tạo database
    db.init_app(app)

    # Khởi tạo Swagger
    swagger = Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    # Đăng ký Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(clinic_bp)
    app.register_blueprint(dentist_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(todo_bp)

    return app

if __name__ == '__main__':
    app = create_app()

    # Tạo các bảng cơ sở dữ liệu khi chạy ứng dụng
    with app.app_context():
        db.create_all()
        print("Tất cả các bảng đã được tạo thành công!")

    app.run(debug=True, host='0.0.0.0', port=6868)