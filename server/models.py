""" INNER WORKINGS OF THE BACKEND: models.py


1. Models:
    - User: allows for role based control between admin and user.
    - Clinic
    - Provider
    - Appointment
    - Patient
    - Form

2. Relationships
    - M2M
        - Patient clinic
        - Patient form
        - Form signature
        - Document file

    - M2O
        - 



"""

from flask_sqlalchemy import SQLAlchemy;
from sqlalchemy.orm import relationship;
from sqlalchemy_serializer import SerializerMixin;

db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ ='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    appointments = relationship('Appointment', back_populates='user')

    serialize_rules = ('-password_hash','-email')

class Clinic(db.Model):
    __tablename__ = 'clinics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)

    providers = relationship('Provider', back_populates='clinics')

class Provider(db.Model, SerializerMixin):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name =db.Column(db.String, nullable=False)
    provider_type = db.Column(db.String, nullable=False)
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.id'))

    clinic = relationship('Clinic', back_populates='providers')

    serialize_rules = ('-providers.clinc')

class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))

    patient = relationship('Patient', back_populates='appointments')
    provider = relationship('Provider')

    serialize_rules = ('-patient.DL_image')

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String, nullable=False)
    DL_image = db.Column(db.LargeBinary)
    rx = db.Column(db.String)

    appointments = relationship('Appointment', secondary='patient_forms')
    clinics = relationship('Clinic', secondary='patient_clinics')

class Form(db.Model):
    __tablename__ = 'forms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    document = db.Column(db.String)

    signature = relationship('FormSignature', back_populates='forms')

class PatientClinc(db.Model):
    __tablename__ = 'patient_clinics'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    clinic_id = db.Column(db.Integer, db.ForeignKey('clinics.id'))

class PatientForm(db.Model):
    __tablename__ = 'patient_forms'

    id = db.Column(db.Integer, primary_key=True)
    patient_id= db.Column(db.Integer, db.ForeignKey('patients.id'))
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'))

class FormSignature(db.Model):
    __tablename__ = 'form_signatures'

    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    signature = db.Column(db.String)

    form = relationship('Form', backpopulates='signatures')
    patient = relationship('Patient', back_populates='signatures')

class DocumentFile(db.Model):
    __tablename__ = 'document_files'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    file_path = db.Column(db.String)
    form_id = db.Column(db.Integer, db.ForeignKey('forms.id'))
    form_signature_id = db.Column(db.Integer, db.ForeignKey('form_signatures.id'))