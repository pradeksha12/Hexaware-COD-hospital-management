class Patient:
    def __init__(self, patient_id=None, first_name=None, last_name=None, dob=None, gender=None, contact_number=None, address=None):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__gender = gender
        self.__contact_number = contact_number
        self.__address = address

    # Getters
    def get_patient_id(self):
        return self.__patient_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_dob(self):
        return self.__dob

    def get_gender(self):
        return self.__gender

    def get_contact_number(self):
        return self.__contact_number

    def get_address(self):
        return self.__address

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def __str__(self):
        return f"Patient ID: {self.__patient_id}, Name: {self.__first_name} {self.__last_name}, DOB: {self.__dob}, Gender: {self.__gender}, Contact: {self.__contact_number}, Address: {self.__address}"
