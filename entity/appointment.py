class Appointment:
    def __init__(self, appointment_id=None, patient_id=None, doctor_id=None, appointment_date=None, description=None):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__description = description

    # Getters
    def get_appointment_id(self):
        return self.__appointment_id

    def get_patient_id(self):
        return self.__patient_id

    def get_doctor_id(self):
        return self.__doctor_id

    def get_appointment_date(self):
        return self.__appointment_date

    def get_description(self):
        return self.__description

    # Setters
    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    def set_appointment_date(self, appointment_date):
        self.__appointment_date = appointment_date

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return f"Appointment ID: {self.__appointment_id}, Patient ID: {self.__patient_id}, Doctor ID: {self.__doctor_id}, Date: {self.__appointment_date}, Description: {self.__description}"
