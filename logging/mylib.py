# mylib.py
import logging



def divide_zero():
    logger = logging.getLogger(__name__)
    logging.info('Message with logging')
    logger.info('Message with logger')
    try:
        1/0
    except ZeroDivisionError as e:
        logging.exception("We are dividing in zero")