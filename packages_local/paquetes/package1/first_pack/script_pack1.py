import os
import pandas
print("pandas was imported")

def fcn_pack1():
    result = {
        'basename': os.path.basename(__file__),
        'dirname': os.path.dirname(__file__),
    }

    print("Hola from pakage1/first_pack(__init__)/script_pack1.py")
    print(f"dirname: {result['dirname']}, basename: {result['basename']}")
    print("package1 is a flat package")

    return result

def second_fcn():
    print("After poetry build")
    print("So, If I change something in script_pack1, it changes!!!!")

if __name__ == "__main__":
    fcn_pack1()