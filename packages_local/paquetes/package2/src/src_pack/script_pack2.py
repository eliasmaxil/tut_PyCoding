import os

import pandas
print("pandas was imported from package2")

def fcn_pack2():
    result = {
        'basename': os.path.basename(__file__),
        'dirname': os.path.dirname(__file__),
    }

    print("Hola from pakage2/src/src_pack(__init__)/script_pack1.py")
    print(f"dirname: {result['dirname']}, basename: {result['basename']}")
    print("package2 is a src package")

    return result


if __name__ == "__main__":
    fcn_pack2()