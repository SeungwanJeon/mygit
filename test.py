import numpy as np

def xmul(a, b):
    # """
    # Multiply stacked matrices A (with shape (s, m, n)) by stacked
    # matrices B (with shape (s, n, p)) to produce an array with
    # shape (s, m, p).
    #
    # Mathematically equivalent to A @ B, but faster in many cases.
    #
    # The arguments are not validated.  The code assumes that A and B
    # are numpy arrays with the same data type and with shapes described
    # above.
    # """
    out = np.empty((a.shape[0], a.shape[1], b.shape[2]), dtype=a.dtype)
    for j in range(a.shape[0]):
        np.matmul(a[j], b[j], out=out[j])
    return out

A = np.random.rand(100, 30, 40)
B = np.random.rand(100, 40, 50)

%timeit A @ B
1.75 ms ± 8.11 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit xmul(A, B)
2.05 ms ± 32.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit np.matmul(A, B)

import numpy as np
from scipy.fftpack import fft
from scipy.fftpack import dct,idct
a=np.random.rand(5,7)
b=np.fft.fft(a,axis=0)
c=np.abs(np.fft.ifft(b,axis=0))
b=dct(a,norm = 'ortho',axis=0)
c=idct(b,norm = 'ortho',axis=0)

%timeit b=fft(np.random.rand(1000))

import numpy as np

a=np.random.rand(5,5)
np.flipud(a)
np.pad(a,)
%timeit np.pad(a,((a.shape[0]-1,0),(0,0)),'reflect')
%timeit np.concatenate((np.flipud(a),a[1:,:]),axis=0)

from scipy.fftpack import dct,idct
%timeit np.fft.fft2(np.concatenate((np.flipud(a),a[1:,:]),axis=0))
%timeit np.fft.fft(dct(a,axis=0),axis=1)



a='성희는 %(abc)s이다'
print(a%{'abc':'바보'})


import reikna.fft
import numpy
shape=(2,2,1); dtype=numpy.float32; axes=0
data = numpy.random.normal(size=shape).astype(dtype)

fft = reikna.fft.fft(data, axes=axes)
fftc = fft.compile(thr)


reikna.fft.helpers
