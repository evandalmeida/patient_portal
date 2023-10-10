

BACKEND:
server/ 
    ├── app.py [Main Flask app]             
    ├── extensions.py [Intializes Flask extensions]      
    ├── models.py [Define databse schema]           
    ├── .env [store environment vars: KEYS]                 
    ├── /admin/
    │        ├── admin_routes.py
    │
    ├── /patient/
    │          ├── patient_routes.py
    │
    ├── /migrations/
    ├── /resources/
    ├── /services/
    ├── /static/
    ├── /templates/
    ├── /utils/




1. cd server/
2. pip install pipenv
3. pipenv install



DEPENDENCIES:
- Flask
    - Flask==2.0.1 
        [python frame work for backend API and web apps]
    - Flask-RESTful==0.3.8  
        [REST API for fullstack apps]
    - Flask-JWT-Extended==4.3.1  
        [JWT is a statless auth mechanism to protect routes via JSON Web Tokens]
    - Flask-SQLAlchemy==2.5.1
        [Allows backend to ORM using PostgreSQL]
    - psycopg2-binary==2.9.9
        [PostgreSQL database adapter to use SQLAlchemy on Python]
    - python-dotenv==0.15.0
        [Loads variables froma an .env file manage configs serpately]
    - gunicorn==20.0.4
        [WSGI server to run Flask in production & replace built in Flask dev server]
    - flask-cors==3.1.1
        [Enables cross origin resource sharing to handle rquest form different origins]

- Sending Emails
    - flask-mail==0.9.1
        [Generates a web-based admin interface for managing application data]

- Optomizing Emails
    - premailer==3.7.0
        [Employs CSS styles to format HTML emails]

- Security
    - flask-security==4.0.3
        [Adds security related features for user auths]

- Database
    - SQLAlchemy==1.3.23
        [Python ORM forms database access to make models, write queries, manage sessions]
    - Flask-Migrate==3.0.1
        [Integrates migratiosn from SQLAlachemy database to Flask so database schema is maitained during updates]
        
- Caching and Background
    - redis==3.5.3
        [In-memory data storage for cache and messages for background tasks]
    - flask-caching==1.10.1
        [provides cachin functionality to improve performance]
    - celery==5.2.7
        [Integrates backgorund tasks with Flask for emails and data processing]
    - pytz>=2020.1
        [set min requriement for python dependency- celery]

- API Documentation and Testing
    - flasgger==0.9.5
        [Generates interactive OpenAPI specs and Swagger UI for documenting the APIs]
    - pytest==6.2.2
        [Unit testing]
    - coverage==5.5
        [Checks test coverage stats to improve test coverage]
    - freezegun==1.1.0
        [Helps with any time issue durn testing]
    - flask-restful-swagger==0.20.0
        [Generates API documentation using Swagger for docoumenting RESTful API]

- Quality and Monitoring
    - flake8==3.9.2
        [Enforces PEP8 styles and finds potential bugs]
    - sentry-sdk==1.31.0
        [Centralized observatbility for tracking errors and logs]

- Utilities for HTTP/Serilization
    - requests==2.25.1
        [HTTP client library for Python to call external APIs]
    - pyjwt==2.1.0
        [Uses HS256 algorithm to encode/decode JWT tokens]
    marshmallow==3.10.0
        [serilization and deserlization library for converting data types to Python objects and JSON]

- Server Side Session Management
    - flask-session==0.4.0
        [Enables server-side session managment]

- Rate Limiting and Access Control
    - flask-limiter==2.1.0
        [Enables rate limiting and IP based access control]

- Async Processing
    - eventlet==0.30.2
        [asyn framework for non blocking i/o operations]

- Scheduling
    - apscheduler==3.7.0
        [scheduling library for running jobs, cron jobs and backgoround]