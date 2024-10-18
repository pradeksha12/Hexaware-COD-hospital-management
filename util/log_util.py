import logging

class LogUtil:
    @staticmethod
    def setup_logging():
        logging.basicConfig(
            filename='hospital_management.log',  # Log file name
            level=logging.INFO,                   # Log level
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)
