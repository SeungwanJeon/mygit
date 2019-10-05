
"""
Multiplies two square matrices together using a *single* block of threads and
global memory only. Each thread computes one element of the resulting matrix.
"""

import numpy as np
from pycuda import driver, compiler, gpuarray, tools

# -- initialize the device
import pycuda.autoinit

kernel_code_template = """
__global__ void MatrixMulKernel(float *a, float *b, float *c)
{
    // 2D Thread ID (assuming that only *one* block will be executed)
    int tx = threadIdx.x;
    int ty = threadIdx.y;

    //int tx = blockIdx.x*blockDim.x + threadIdx.x;
    //int ty = blockIdx.x*blockDim.x + threadIdx.x;
    //printf("%%d %%d %%d %%d\\n",threadIdx.x,threadIdx.y,blockIdx.x,blockIdx.y,blockDim.x);

    // Pvalue is used to store the element of the matrix
    // that is computed by the thread
    float Pvalue = 0;

    // Each thread loads one row of M and one column of N,
    //   to produce one element of P.
    for (int k = 0; k < %(MATRIX_SIZE)s; ++k) {
        float Aelement = a[ty * %(MATRIX_SIZE)s + k];
        float Belement = b[k * %(MATRIX_SIZE)s + tx];
        Pvalue += Aelement * Belement;
    }

    // Write the matrix to device memory;
    // each thread writes one element
    c[ty * %(MATRIX_SIZE)s + tx] = Pvalue;
}
"""

# define the (square) matrix size
#  note that we'll only use *one* block of threads here
#  as a consequence this number (squared) can't exceed max_threads,
#  see http://documen.tician.de/pycuda/util.html#pycuda.tools.DeviceData
#  for more information on how to get this number for your device
MATRIX_SIZE = 2

# create two random square matrices
a_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
b_cpu = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)

# compute reference on the CPU to verify GPU computation
#%timeit c_cpu = np.dot(a_cpu, b_cpu)
c_cpu = np.dot(a_cpu, b_cpu)

# transfer host (CPU) memory to device (GPU) memory
a_gpu = gpuarray.to_gpu(a_cpu)
b_gpu = gpuarray.to_gpu(b_cpu)

# create empty gpu array for the result (C = A * B)
c_gpu = gpuarray.empty((MATRIX_SIZE, MATRIX_SIZE), np.float32)

# get the kernel code from the template
# by specifying the constant MATRIX_SIZE
kernel_code = kernel_code_template % {
    'MATRIX_SIZE': MATRIX_SIZE
    }

# compile the kernel code
mod = compiler.SourceModule(kernel_code)

# get the kernel function from the compiled module
matrixmul = mod.get_function("MatrixMulKernel")

# call the kernel on the card
#%timeit matrixmul(a_gpu, b_gpu,c_gpu,block = (8, 8, 1))
matrixmul(
    # inputs
    a_gpu, b_gpu,
    # output
    c_gpu,
    block = (2, 2, 1),
    )

# print the results
print ("-" * 80)
print ("Matrix A (GPU):")
print (a_gpu.get())

print ("-" * 80)
print ("Matrix B (GPU):")
print (b_gpu.get())

print ("-" * 80)
print ("Matrix C (GPU):")
print (c_gpu.get())

print ("-" * 80)
print ("CPU-GPU difference:")
print (c_cpu - c_gpu.get())

print(np.allclose(c_cpu, c_gpu.get()))
