# Architecture

```bash
    ├── .env
    ├── app.py
    ├── config.py
    ├── migrations/
    ├── scripts/
    │   └── run_postgres.sh
    ├── src/
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── controllers/
    │   │   │   ├── __init__.py
    │   │   │   ├── auth_controller.py
    │   │   │   ├── chat_controller.py
    │   │   │   ├── clinic_controller.py
    │   │   │   ├── dentist_controller.py
    │   │   │   └── todo_controller.py
    │   │   ├── schemas/
    │   │   │   ├── __init__.py
    │   │   │   ├── auth.py
    │   │   │   ├── chat.py
    │   │   │   ├── clinic.py
    │   │   │   ├── dentist.py
    │   │   │   └── todo.py
    │   │   ├── middleware.py
    │   │   ├── responses.py
    │   │   └── requests.py
    │   ├── infrastructure/     # Data layer (ORM + Repository + external services)
    │   │   ├── __init__.py
    │   │   ├── databases/
    │   │   │   ├── __init__.py
    │   │   │   ├── appointment_model.py
    │   │   │   ├── base.py
    │   │   │   ├── chat_model.py
    │   │   │   ├── clinic_model.py
    │   │   │   ├── dentist_model.py
    │   │   │   ├── todo_model.py
    │   │   │   └── user_model.py
    │   │   ├── repositories/  # Repository: CRUD DB, map Domain ↔ ORM
    │   │   │   ├── __init__.py
    │   │   │   ├── appointment_repository.py
    │   │   │   ├── chat_repository.py
    │   │   │   ├── clinic_repository.py
    │   │   │   ├── dentist_repository.py
    │   │   │   ├── itodo_repository.py
    │   │   │   └── todo_repository.py
    │   │   └── models/ 
    │   │       └── ...  # Lưu các SQLAlchemy models tại đây
    │   ├── domain/     # Core Domain (Entities, VO, Domain rules)
    │   │   ├── __init__.py
    │   │   ├── constants.py
    │   │   ├── exceptions.py
    │   │   └── models/     # (Optional) nơi lưu models khác (nếu cần)
    │   │       ├── __init__.py
    │   │       ├── ...
    │   ├── services/    # Application layer (use-cases)
    │   │   ├── __init__.py
    │   │   ├── appointment_service.py
    │   │   ├── auth_service.py
    │   │   ├── chat_service.py
    │   │   ├── clinic_service.py
    │   │   └── todo_service.py
    │   ├── app.py
    │   ├── config.py
    │   ├── cors.py
    │   ├── create_app.py
    │   ├── dependency_container.py
    │   ├── error_handler.py
    │   └── logging.py
```
# Domain Layer 
```
 domain/     
   ├── __init__.py
   ├── constants.py
   ├── exceptions.py
   └── models/     
         ├── __init__.py
         ├── appointment.py
         ├── clinic.py
         ├── conversation.py
         ├── dentist.py
         ├── message.py
         ├── service.py
         ├── todo.py
         └── user.py
```
