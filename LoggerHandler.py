import pytest
import logging


@pytest.mark.usefixtures("setup")
class LoggerHandler:

    def get_logger(self):
        logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler('./logs/logfile.log', 'wb')
        formatter = logging.Formatter('%(asctime)s :%(levelname)s : %(name)s :%(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.INFO)
        return logger
