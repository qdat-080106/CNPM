from src.api.controllers.todo_controller import bp as todo_bp

def register_routes(app):
    app.register_blueprint(todo_bp) 
from src.api.controllers.auth_controller import auth_bp
from src.api.controllers.clinic_controller import clinic_bp
from src.api.controllers.dentist_controller import dentist_bp
from src.api.controllers.chat_controller import chat_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(clinic_bp)
    app.register_blueprint(dentist_bp)
    app.register_blueprint(chat_bp)