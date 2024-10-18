from dao.hospital_service_impl import HospitalServiceImpl
from entity.appointment import Appointment
from exception.patient_not_found_exception import PatientNotFoundException
from exception.doctor_not_found_exception import DoctorNotFoundException

def main():
    service = HospitalServiceImpl()

    while True:
        print("\n=== Hospital Management System ===")
        print("1. Schedule Appointment")
        print("2. Update Appointment")
        print("3. Cancel Appointment")
        print("4. Get Appointment by ID")
        print("5. Get Appointments for Patient")
        print("6. Get Appointments for Doctor")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Show available doctors with their IDs and specializations
            doctors = service.get_all_doctors()  # Method to fetch all doctors
            print("\nAvailable Doctors:")
            for doctor in doctors:
                print(f"ID: {doctor.get_doctor_id()}, Name: {doctor.get_first_name()} {doctor.get_last_name()}, Specialization: {doctor.get_specialization()}")


            # Schedule an appointment
            try:
                appointment_id = int(input("Enter appointment ID: "))
                patient_id = int(input("Enter patient ID: "))
                doctor_id = int(input("Enter doctor ID: "))
                appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
                description = input("Enter description: ")
                appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
                
                if service.schedule_appointment(appointment):
                    print("Appointment scheduled successfully.")
                else:
                    print("Failed to schedule appointment.")
            except Exception as e:
                print(f"Error scheduling appointment: {e}")

        elif choice == '2':
            # Update an appointment
            try:
                appointment_id = int(input("Enter appointment ID to update: "))
                patient_id = int(input("Enter new patient ID: "))
                doctor_id = int(input("Enter new doctor ID: "))
                appointment_date = input("Enter new appointment date (YYYY-MM-DD): ")
                description = input("Enter new description: ")
                appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
                
                if service.update_appointment(appointment):
                    print("Appointment updated successfully.")
                else:
                    print("Failed to update appointment.")
            except Exception as e:
                print(f"Error updating appointment: {e}")

        elif choice == '3':
            # Cancel an appointment
            try:
                appointment_id = int(input("Enter appointment ID to cancel: "))
                if service.cancel_appointment(appointment_id):
                    print("Appointment cancelled successfully.")
                else:
                    print("Failed to cancel appointment.")
            except Exception as e:
                print(f"Error cancelling appointment: {e}")

        elif choice == '4':
            # Get appointment by ID
            try:
                appointment_id = int(input("Enter appointment ID: "))
                appointment = service.get_appointment_by_id(appointment_id)
                if appointment:
                    print(f"Retrieved appointment: {appointment}")
                else:
                    print("Appointment not found.")
            except PatientNotFoundException as e:
                print(e)
            except Exception as e:
                print(f"Error retrieving appointment: {e}")

        elif choice == '5':
            # Get appointments for a patient
            try:
                patient_id = int(input("Enter patient ID: "))
                appointments = service.get_appointments_for_patient(patient_id)
                
                if appointments is not None:
                    if appointments:
                        print(f"Retrieved {len(appointments)} appointments for patient ID {patient_id}:")
                        for appointment in appointments:
                            print(appointment)
                    else:
                        print("No appointments found for this patient.")
                else:
                    print(f"Please enter a valid integer for patient ID.")
                    
            except ValueError:
                print("Please enter a valid integer for patient ID.")
            except Exception as e:
                print(f"Error retrieving appointments for patient: {e}")

        elif choice == '6':
            # Get appointments for a doctor
            try:
                doctor_id = int(input("Enter doctor ID: "))
                appointments = service.get_appointments_for_doctor(doctor_id)
                if appointments:
                    print(f"Retrieved {len(appointments)} appointments for doctor ID {doctor_id}:")
                    for appointment in appointments:
                        print(appointment)
                else:
                    print("No appointments found for this doctor.")
            except Exception as e:
                print(f"Error retrieving appointments for doctor: {e}")

        elif choice == '7':
            print("Your health is an investment not an expense")
            print("Logging off...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
