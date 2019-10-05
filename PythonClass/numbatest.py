from numba import jit
import numpy as np
# print(numba.__version__)

def MultiCal(a,b):
    return ((a*b)**0.5)/(a + b) + ((a*b)**0.5)/(a + b)

@jit(nopython=True, cache=True)
def MultiCalNumba(a,b):
    return ((a*b)**0.5)/(a + b) + ((a*b)**0.5)/(a + b)

def PurePythonCal():
    result = sum([MultiCal(i, i+1) for i in range(10000000)])

def NumbaCal():
    result = np.sum([MultiCalNumba(i, i+1) for i in range(10000000)])
