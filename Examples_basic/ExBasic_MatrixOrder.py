import numpy as np

x=np.random.rand(256,256)

x_c=np.asanyarray(x,dtype=np.float32,order='C') # C style
x_f=np.asanyarray(x,dtype=np.float32,order='F') # Fortran style

%timeit np.sum(x_c,axis=0)
%timeit np.sum(x_f,axis=0)
""" output
31.1 µs ± 139 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
17.7 µs ± 95.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
"""

%timeit np.sum(x_c,axis=1)
%timeit np.sum(x_f,axis=1)
""" output
17.7 µs ± 53.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
31 µs ± 71.4 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
"""
