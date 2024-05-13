import logging

class Logger:

    def __init__(self, name, log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Create a file handler for w