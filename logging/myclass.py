import logging

# This means that logger names track the package/module hierarchy, 
# and it’s intuitively obvious where events are logged just 
# from the logger name.

format="%(asctime)-4s - %(name)s - %(levelname)-4s - [%(filename)s:%(lineno)d]: %(message)s"

logger = logging.getLogger(__name__)

handler = logging.FileHandler("file2.log", mode="w")
formatter = logging.Formatter(format)
handler.setFormatter(formatter)
logger.addHandler(handler)


class myclass(object):
    def __init__(self, hola="THE INIT VAR"):
        self.hola = hola

    def print_hola(self):

        print(self.hola)
        logger.error(f'logging.getLogger(__name__)')
        logging.critical(f'{self.hola} was printed too')

    @property
    def adec(self):
        logging.warning(f'{self.hola} in a decorator')
        return self.hola



