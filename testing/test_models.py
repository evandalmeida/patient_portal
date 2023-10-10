import pytest
from server.models import db, User, Clinic, Provider, Appointment, Patient, Form, PatientClinic, PatientForm, FormSignature, DocumentFile



@pytest.fixture(scope='module')
def init_database():
    """
    Create a database with some initial data for testing.
    """
    db.create_all()

    # Create test data here
    user = User(username='testuser', password_hash='hashed_password', role='user', email='test@example.com')
    clinic = Clinic(name='Test Clinic', address='123 Main St', city='Test City', zip_code=12345)
    provider = Provider(first_name='John', last_name='Doe', provider_type='Type A', clinic=clinic)
    appointment = Appointment(date='2023-01-01', time='10:00:00', patient=None, provider=provider)
    patient = Patient(first_name='Jane', last_name='Smith', dob='1990-01-01', address='456 Elm St', DL_image=None, rx='RX123')
    form = Form(name='Test Form', document='Test Document')
    patient_clinic = PatientClinic(patient=patient, clinic=clinic)
    patient_form = PatientForm(patient=patient, form=form)
    form_signature = FormSignature(form=form, patient=patient, signature='Test Signature')
    document_file = DocumentFile(file_name='test_file.txt', file_path='/path/to/file', form=form, form_signature=form_signature)

    db.session.add(user)
    db.session.add(clinic)
    db.session.add(provider)
    db.session.add(appointment)
    db.session.add(patient)
    db.session.add(form)
    db.session.add(patient_clinic)
    db.session.add(patient_form)
    db.session.add(form_signature)
    db.session.add(document_file)

    db.session.commit()

    yield db

    db.drop_all()


def test_user_model(init_database):
    """
    Test User model.
    """
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    assert user.username == 'testuser'
    assert user.role == 'user'


def test_clinic_model(init_database):
    """
    Test Clinic model.
    """
    clinic = Clinic.query.filter_by(name='Test Clinic').first()
    assert clinic is not None
    assert clinic.name == 'Test Clinic'


def test_provider_model(init_database):
    """
    Test Provider model.
    """
    provider = Provider.query.filter_by(first_name='John', last_name='Doe').first()
    assert provider is not None
    assert provider.first_name == 'John'
    assert provider.provider_type == 'Type A'
    assert provider.clinic is not None


def test_appointment_model(init_database):
    """
    Test Appointment model.
    """
    appointment = Appointment.query.filter_by(date='2023-01-01', time='10:00:00').first()
    assert appointment is not None
    assert appointment.provider is not None
    assert appointment.provider.first_name == 'John'
    assert appointment.patient is None  # In this test, the appointment has no patient assigned.


def test_patient_model(init_database):
    """
    Test Patient model.
    """
    patient = Patient.query.filter_by(first_name='Jane', last_name='Smith').first()
    assert patient is not None
    assert patient.dob == '1990-01-01'
    assert patient.rx == 'RX123'
    assert len(patient.appointments) == 0  # In this test, the patient has no appointments assigned.
    assert len(patient.clinics) == 1  # The patient should be associated with one clinic.


def test_form_model(init_database):
    """
    Test Form model.
    """
    form = Form.query.filter_by(name='Test Form').first()
    assert form is not None
    assert form.document == 'Test Document'


def test_patient_clinic_relationship(init_database):
    """
    Test Patient-Clinic relationship.
    """
    patient = Patient.query.filter_by(first_name='Jane', last_name='Smith').first()
    clinic = Clinic.query.filter_by(name='Test Clinic').first()
    assert patient is not None
    assert clinic is not None
    assert clinic in patient.clinics


def test_patient_form_relationship(init_database):
    """
    Test Patient-Form relationship.
    """
    patient = Patient.query.filter_by(first_name='Jane', last_name='Smith').first()
    form = Form.query.filter_by(name='Test Form').first()
    assert patient is not None
    assert form is not None
    assert form in patient.forms


def test_form_signature_model(init_database):
    """
    Test FormSignature model.
    """
    form_signature = FormSignature.query.first()
    assert form_signature is not None
    assert form_signature.signature == 'Test Signature'
    assert form_signature.form is not None
    assert form_signature.patient is not None


def test_document_file_model(init_database):
    """
    Test DocumentFile model.
    """
    document_file = DocumentFile.query.first()
    assert document_file is not None
    assert document_file.file_name == 'test_file.txt'
    assert document_file.file_path == '/path/to/file'
    assert document_file.form is not None
    assert document_file.form_signature is not None


if __name__ == '__main__':
    pytest.main()
