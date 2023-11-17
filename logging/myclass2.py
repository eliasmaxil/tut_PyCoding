import logging

# The whole class is connected to logger
logger = logging.getLogger(__name__)  # Dit is wenselijk

class myclass2(object):
    def __init__(self, hola="hola"):
        self.hola = hola

    def log_adios(self):
        logger.info('Loggeando desde myclass2.py')
        logger.info(f'{self.hola} y adios con logger')
        logger.warning(f'{self.hola} y adios con logging')

    @property
    def adec(self):
        logger.warning(f'{self.hola} in a decorator')
        return self.hola

if __name__ == '__main__':

    format="%(asctime)-4s - %(name)s - %(levelname)-4s - [%(filename)s:%(lineno)d]: %(message)s"
    logging.basicConfig(
        level=logging.DEBUG,
        filename="file3.log",
        filemode="w",
        format=format, 
        )

    
    
    myclass2().log_adios()
    myclass2().adec

