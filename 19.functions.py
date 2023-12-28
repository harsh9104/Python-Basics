"""
Functions :
           It has 3 types.
           (i) In-Built Functions  
          (ii) Module Functions
         (iii) User-Defined Functions

(i) : int(), str(), bool()
(ii) : math
(iii) :
SYNTAX : def + function_name + (parameters) + :
         # statement
         return expression
"""
#(ii)
import math              #use to import math library in code.
(print(dir(math)))       #use to see functions available in math library.

from math import *       #use to access every functions from math library.
print(sqrt(4))

from math import sqrt    #use to access only sqrt function from math library.
print(sqrt(16))

#(iii)
def print_sum(first, second):    #SYNTAX
    print(first + second)

print_sum(1, 3)

def print_sum(first, second=5):
    print(first + second)

print_sum(1)