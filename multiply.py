import numpy as np

def multiply():
    a = np.ndarray(shape=(3,3), dtype=int, order='F')
    b = np.ndarray(shape=(3,3), dtype=int, order='F')
    return a*b
print("Answer is",multiply())