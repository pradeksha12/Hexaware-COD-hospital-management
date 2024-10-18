import pyodbc
from util.property_util import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        # Directly hardcoding the connection details for testing
        connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LENOVO\\SQLEXPRESS;DATABASE=HospitalDB;Trusted_Connection=yes;TrustServerCertificate=yes;'
        conn = pyodbc.connect(connection_string)
        return conn

