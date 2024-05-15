import logging


class LogGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename="C:/Users/bgulh/nopCommerceApp/DemoNopCommerce/logs", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
