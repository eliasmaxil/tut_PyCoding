import logging
import mylib
import myclass
import myclass2

format="%(asctime)-4s - %(name)s - %(levelname)-4s - [%(filename)s:%(lineno)d]: %(message)s"

def main():
    # mylib.py
    logging.info('Started myapp')
    mylib.divide_zero()
    logging.info('Finished mylib.do_something')
    logging.debug('myapp: %s, and the, %s', 'Variable1', 'Variable2')
    # myclass.py
    obj = myclass.myclass()
    obj.print_hola()
    logging.debug(f'{obj.adec} logged from myclass @property')
    # myclass2.py
    obj2 = myclass2.myclass2()
    obj2.log_adios()
    logging.debug('========')
    hola = obj2.adec
    logging.warning(f'{hola} was returned and this is its message')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename="file1.log",
        filemode="w",
        format=format, 
        )
    main()