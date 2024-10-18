-- Create Database
CREATE DATABASE HospitalDB;


-- Use the Database
USE HospitalDB;


-- Create Patient Table
CREATE TABLE Patient (
    patientId INT PRIMARY KEY,
    firstName NVARCHAR(50) NOT NULL,
    lastName NVARCHAR(50) NOT NULL,
    dateOfBirth DATE NOT NULL,
    gender CHAR(1) CHECK (gender IN ('M', 'F', 'O')),  -- M: Male, F: Female, O: Other
    contactNumber NVARCHAR(15),
    address NVARCHAR(255)
);


-- Create Doctor Table
CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY,
    firstName NVARCHAR(50) NOT NULL,
    lastName NVARCHAR(50) NOT NULL,
    specialization NVARCHAR(100) NOT NULL,
    contactNumber NVARCHAR(15)
);


-- Create Appointment Table
CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY,
    patientId INT NOT NULL,
    doctorId INT NOT NULL,
    appointmentDate DATETIME NOT NULL,
    description NVARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);


INSERT INTO Patient (patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address) VALUES
(1, 'Rahul', 'Sharma', '1995-05-15', 'M', '9876543210', ' 5 Sohini Bldg, D J Rd, Vile Parle(w), Delhi'),
(2, 'Priya', 'Verma', '1988-08-22', 'F', '9876543211', '350, Avenue Road, Avenue Road, Noida'),
(3, 'Anil', 'Kumar', '1992-03-10', 'M', '9876543212', '26/3, 4th Cross, Malleshwaram, Gurgaon'),
(4, 'Sita', 'Patel', '1990-01-01', 'F', '9876543213', '514, Sarai Pipal Thala Extn, G T Road, Adarsh Nagar, Ahmedabad'),
(5, 'Amit', 'Singh', '1994-11-11', 'M', '9876543214', 'B-60, Shanti Comm Centre, Nagar Seth Vando, Gheekanta, Mumbai'),
(6, 'Neha', 'Reddy', '1985-12-30', 'F', '9876543215', '131, Sector 3, Bangalore'),
(7, 'Vikram', 'Iyer', '1993-04-25', 'M', '9876543216', '81,newno 163 1st Floor, Thambu Chetty Street, Chennai'),
(8, 'Pooja', 'Nair', '1989-02-20', 'F', '9876543217', '3, Deep Chambers, Mahajan Lane, Pune'),
(9, 'Suresh', 'Jha', '1996-07-15', 'M', '9876543218', '67/7/8 Phase 1, 67/7, 67/8 Phase 1, Vatva, Kolkata'),
(10, 'Meena', 'Das', '1987-09-09', 'F', '9876543219', '104 A, Big Splash, Sector 17, Vashi, Hyderabad');


INSERT INTO Doctor (doctorId, firstName, lastName, specialization, contactNumber) VALUES
(1, 'Rajesh', 'Menon', 'Cardiology', '9999888877'),
(2, 'Sunita', 'Kapoor', 'Pediatrics', '9999888866'),
(3, 'Kiran', 'Bhatia', 'Orthopedics', '9999888855'),
(4, 'Ravi', 'Malhotra', 'Dermatology', '9999888844'),
(5, 'Tanvi', 'Ahuja', 'Neurology', '9999888833'),
(6, 'Nikhil', 'Nair', 'General Medicine', '9999888822'),
(7, 'Anita', 'Verma', 'Gynecology', '9999888811'),
(8, 'Sanjay', 'Sharma', 'ENT', '9999888800'),
(9, 'Rohit', 'Gupta', 'Urology', '9999888799'),
(10, 'Priyanka', 'Desai', 'Ophthalmology', '9999888788');

INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description) VALUES
(1, 1, 1, '2024-10-25 10:00:00', 'Routine check-up'),
(2, 2, 2, '2024-10-26 11:00:00', 'Child vaccination'),
(3, 3, 3, '2024-10-27 09:30:00', 'Fracture consultation'),
(4, 4, 4, '2024-10-28 12:00:00', 'Skin rash treatment'),
(5, 5, 5, '2024-10-29 14:00:00', 'Neurological assessment'),
(6, 6, 6, '2024-10-30 15:30:00', 'General health check'),
(7, 7, 7, '2024-11-01 16:00:00', 'Gynecological check-up'),
(8, 8, 8, '2024-11-02 10:15:00', 'Hearing test'),
(9, 9, 9, '2024-11-03 11:45:00', 'Kidney stone consultation'),
(10, 10, 10, '2024-11-04 13:00:00', 'Vision test');

select * from Appointment