import logging

class Logger:

    def __init__(self, name, log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Create a file handler for writing log files
        log_file_path = 'runtime.log'
        file_handler = logging.FileHandler(log_file_path)

        # Create a console handler for printing logs to the console
