import configparser

class PropertyUtil:
    @staticmethod
    def get_property_string(file_name):
        config = configparser.ConfigParser()
        config.read(file_name)

        # Print sections for debugging
        print("Loaded sections:", config.sections())

        # Check if the DATABASE section exists
        if 'DATABASE' not in config:
            raise KeyError("DATABASE section is missing in the configuration file.")

        driver = config['DATABASE']['driver']
        server = config['DATABASE']['server']
        database = config['DATABASE']['database']
        trusted_connection = config['DATABASE'].get('trusted_connection', 'no')
        trust_server_certificate = config['DATABASE'].get('trust_server_certificate', 'no')

        # Construct connection string based on the properties
        connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};'
        if trusted_connection.lower() == 'yes':
            connection_string += 'Trusted_Connection=yes;'
        if trust_server_certificate.lower() == 'yes':
            connection_string += 'TrustServerCertificate=yes;'

        return connection_string
