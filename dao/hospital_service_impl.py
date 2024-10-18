import pyodbc
from entity.appointment import Appointment
from entity.doctor import Doctor
from entity.patient import Patient
from dao.hospital_service_interface import IHospitalService
from util.db_conn_util import DBConnUtil
from util.log_util import LogUtil
from exception.patient_not_found_exception import PatientNotFoundException
from exception.doctor_not_found_exception import DoctorNotFoundException

class HospitalServiceImpl(IHospitalService):
    
    def __init__(self):
        LogUtil.setup_logging()  # Setup logging when the service is initialized

    def get_appointment_by_id(self, appointment_id):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE appointmentId = ?", appointment_id)
            result = cursor.fetchone()
            if result:
                LogUtil.log_info(f"Retrieved appointment: {result}")
                return Appointment(*result)
            else:
                raise PatientNotFoundException(f"No appointment found with ID {appointment_id}")
        except Exception as e:
            LogUtil.log_error(f"Error retrieving appointment: {e}")
        finally:
            conn.close()

    def get_appointments_for_patient(self, patient_id):
        conn = DBConnUtil.get_connection()
        appointments = []
        try:
            cursor = conn.cursor()

            # Check if the patient exists in the database
            cursor.execute("SELECT * FROM Patient WHERE patientId = ?", (patient_id,))
            patient = cursor.fetchone()
            if patient is None:
                raise PatientNotFoundException(f"Patient ID {patient_id} does not exist in the Database.")

            # If patient exists, fetch the appointments
            cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", (patient_id,))
            rows = cursor.fetchall()
            if not rows:
                return None  # No appointments found

            for row in rows:
                appointment = Appointment(appointment_id=row[0], patient_id=row[1], doctor_id=row[2], appointment_date=row[3], description=row[4])
                appointments.append(appointment)

        except PatientNotFoundException as e:
            print(e)  # Handle patient not found
            return None
        except Exception as e:
            print(f"Error fetching appointments: {e}")
        finally:
            cursor.close()
            conn.close()

        return appointments


    def get_appointments_for_doctor(self, doctor_id):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", doctor_id)
            results = cursor.fetchall()
            appointments = [Appointment(*row) for row in results]  # Convert each row to Appointment object
            LogUtil.log_info(f"Retrieved {len(appointments)} appointments for doctor ID {doctor_id}")
            return appointments
        except Exception as e:
            LogUtil.log_error(f"Error retrieving appointments for doctor {doctor_id}: {e}")
        finally:
            conn.close()

    def schedule_appointment(self, appointment):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?, ?)",
                           (appointment.get_appointment_id(), appointment.get_patient_id(), appointment.get_doctor_id(),
                            appointment.get_appointment_date(), appointment.get_description()))
            conn.commit()
            LogUtil.log_info(f"Scheduled appointment: {appointment}")
            return True
        except Exception as e:
            LogUtil.log_error(f"Error scheduling appointment: {e}")
            return False
        finally:
            conn.close()
    def get_all_doctors(self):
        conn = DBConnUtil.get_connection()  # Ensure you are getting the connection
        doctors = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Doctor")
            rows = cursor.fetchall()
            for row in rows:
                doctor = Doctor(doctor_id=row[0], first_name=row[1], last_name=row[2], specialization=row[3], contact_number=row[4])
                doctors.append(doctor)
        except Exception as e:
            print(f"Error fetching doctors: {e}")
        finally:
            cursor.close()
            conn.close()
        return doctors


    def update_appointment(self, appointment):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Appointment SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? WHERE appointmentId = ?",
                           (appointment.get_patient_id(), appointment.get_doctor_id(),
                            appointment.get_appointment_date(), appointment.get_description(),
                            appointment.get_appointment_id()))
            conn.commit()
            LogUtil.log_info(f"Updated appointment: {appointment}")
            return True
        except Exception as e:
            LogUtil.log_error(f"Error updating appointment: {e}")
            return False
        finally:
            conn.close()

    def cancel_appointment(self, appointment_id):
        try:
            conn = DBConnUtil.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", appointment_id)
            conn.commit()
            LogUtil.log_info(f"Cancelled appointment with ID: {appointment_id}")
            return True
        except Exception as e:
            LogUtil.log_error(f"Error cancelling appointment {appointment_id}: {e}")
            return False
        finally:
            conn.close()
