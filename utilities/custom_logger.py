import logging

class Log_Maker:
    @staticmethod
    def log():
        logging.basicConfig(filename="nopcommerce-hybrid-framework/logs/nopcommerce.log", format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger