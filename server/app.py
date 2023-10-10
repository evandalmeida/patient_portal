
from flask import Flask, jsonify, request

# flask extensions
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

# import to load sensitve data securely  
from dotenv import load_dotenv
import os

# user route imports 
from admin_routes import admin_bp
from patient_routes import patient_bp


""" INNER WORKINGS OF THE BACKEND: app.py
1. Obviously import Flask
    - JWT
    - RESTful
    - SQLAlchemy
    - Migrate
    - Api
    - os module for storing sentive information 
    - dotenv to load enviroment variables from .env ()

2. Load
    - Environment variables
    - App
    - Configurations with JWT secret key for security 
    - SQLAlchemy
    - Migrate

3. Create RESTful API instance

4. Create JWT Manager to handle the JWT token encoding/decoding

5. CORS configuration for backend-frontend.

6. As above and beyond, use errror handler, hold me accountable to catching errors.
    - 404 resoruce not found
    - 505 internal server error
"""

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

jwt = JWTManager(app)

cors = CORS(
    app,
    resources={r'/api/*':{
    'origins': 'hhtp://localhost:4000',
    'methods': ['GET', 'POST', 'PATCH', 'DELETE']
    }}
)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'Resource not found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message':'Internal server error'}), 500 


""" INNER WORKINGS OF THE BACKEND: app.py (continued)
Application INTIALIZED with porper error handling.

7. Protected route and login route are ascessible to everyone.

8. Adminstrative and patient routes were seperated into two files to apporiately discern Roles)
    - import both admin and patient routes
    - assign routes to respective URL endpoints
"""

@app.get('/protected')
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    return jsonify({'message':f'Hellow, [current_user]! This is a protected route'})

@app.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'user' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'messgae':'Invalid username or password'}), 401

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(patient_bp, url_prefix='/patient')

if __name__ =='__main__':
    app.run(port=4000, debug=True)