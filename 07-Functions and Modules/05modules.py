'''There are some pre written code which can be accessed in python. This pre written
code can be called as modules. Modules can be of 2 types 
- Internal Modules - already present in python and can be impoirted by import function.
- External Modules - These include few externsl libraries that can be installed using pip 
or those which we make ourselves'''

import math

print(math.sqrt(78))
print(math.cbrt(729))
print(pow(3,4))

# I have created a module my module, and imported here.
import mymodule

print(mymodule.title("Deepanshu",19))