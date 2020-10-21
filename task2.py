
import pandas as pd
import numpy as np
import math

q = 2*1.602e-19
U_0 = 100
m = 6.64e-27
f_rf = 1e6

def equ(i):
       
    v_i = math.sqrt((i*q*U_0*math.sin(math.pi/4))/(2*m))
    
    return (1/f_rf)*v_i


l = [equ(i) for i in range(20)]

print(l)


"""vfunc = np.vectorize(equ, otypes=[float])   ## Vectorize

for i in range(20):
    vfunc(i)
    
print(vfunc)
print(type(vfunc))
"""
