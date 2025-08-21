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
    │   ├── infrastructure/   
    │   │   ├── __init__.py
    │   │   ├── ...
    │   │   └── models/ 
    │   │       └── ...  
    │   ├── domain/     
    │   │   ├── __init__.py
    │   │   ├── constants.py
    │   │   ├── exceptions.py
    │   │   └── models/     
    │   │       ├── __init__.py
    │   │       ├── ...
    │   ├── services/    
    │   │   ├── __init__.py
    │   │   ├── ...
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
# Services Layer
```
src/
└── services/                               
    ├── __init__.py
    ├── auth_service.py                      
    ├── clinic_service.py                    
    ├── dentist_service.py                   
    ├── appointment_service.py               
    ├── chat_service.py                      
    └── todo_service.py
```
# Infrastructure Layer
```
src/
└── infrastructure/                               
    ├── __init__.py
    ├── databases/                                
    │   ├── __init__.py
    │   ├── base.py                               
    │   ├── user_model.py                          
    │   ├── clinic_model.py                       
    │   ├── dentist_model.py                       
    │   ├── appointment_model.py                   
    │   ├── chat_model.py                         
    │   └── todo_model.py                         
    ├── repositories/                             
    │   ├── __init__.py
    │   ├── user_repository.py
    │   ├── clinic_repository.py
    │   ├── dentist_repository.py
    │   ├── appointment_repository.py
    │   ├── chat_repository.py
    │   └── todo_repository.py
    └── models/                                  
        └── ...                                   
```
