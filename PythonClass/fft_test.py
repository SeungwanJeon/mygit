import numpy as np
import scipy

x=np.random.rand(int(1e6))
%timeit fft_np=np.fft.fft(x)
%timeit fft_scipy=scipy.fftpack.fft(x)

x=np.random.rand(2**10)
%timeit fft_np=np.fft.fft(x)
%timeit fft_scipy=scipy.fftpack.fft(x)

x=np.random.rand(2**20)
%timeit fft_np=np.fft.fft(x)
%timeit fft_scipy=scipy.fftpack.fft(x)


x=np.random.rand(3,1)
np.fft.fft(x,axis=0)
np.fft.rfft(x,axis=0)

np.abs(scipy.fftpack.dct(x,axis=0))
np.abs(scipy.fftpack.fft(x,axis=0))
