import os
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

class Config:
    """Cấu hình cơ bản cho ứng dụng."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-super-secret-key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
    TESTING = os.environ.get('TESTING', 'False').lower() in ['true', '1']
    
    # Sửa tên biến này thành SQLALCHEMY_DATABASE_URI để Flask-SQLAlchemy nhận diện
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///default.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'

    # Thêm cấu hình Swagger/Flasgger vào lớp này
    SWAGGER_TEMPLATE = {
        "swagger": "2.0",
        "info": {
            "title": "Dental Clinic API",
            "description": "API for managing dental clinic services",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": ["http", "https"],
        "consumes": ["application/json"],
        "produces": ["application/json"],
    }

class DevelopmentConfig(Config):
    """Cấu hình cho môi trường phát triển."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///dev.db'

class TestingConfig(Config):
    """Cấu hình cho môi trường kiểm thử."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///test.db'

class ProductionConfig(Config):
    """Cấu hình cho môi trường production."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///prod.db'

# Dictionary để app.py có thể chọn cấu hình phù hợp
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}