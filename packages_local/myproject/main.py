import pandas

from first_pack.script_pack1 import fcn_pack1

print("Test the import from package1")
fcn_pack1()
print("-----------------")

from first_pack.script_pack1 import second_fcn
second_fcn()
print("-----------------")

# Importing package2

from src_pack.script_pack2 import fcn_pack2

fcn_pack2()
print("-----------------")