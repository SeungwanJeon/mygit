import numpy as np
from pycuda import driver, compiler, gpuarray, tools

# -- initialize the device
import pycuda.autoinit

kernel_code_template = """
__global__ void mycuCopy(float *odata, const float *idata)
{
  int x = blockIdx.x * blockDim.x + threadIdx.x;
  int y = blockIdx.y * blockDim.y + threadIdx.y;
  if ((x < %(size_x)s) && (y < %(size_y)s)) {
    odata[y*%(size_x)s + x] = idata[y*%(size_x)s + x];
  }
}
"""

# define the (square) matrix size
#  note that we'll only use *one* block of threads here
#  as a consequence this number (squared) can't exceed max_threads,
#  see http://documen.tician.de/pycuda/util.html#pycuda.tools.DeviceData
#  for more information on how to get this number for your device
MATRIX_SIZE_y = 4
MATRIX_SIZE_x = 3

# create two random square matrices
a_cpu = np.random.randn(MATRIX_SIZE_y, MATRIX_SIZE_x).astype(np.float32)
c_cpu = a_cpu.copy()

# transfer host (CPU) memory to device (GPU) memory
# Fortran style order로 바꾸어 주면 gpu로 넘겨도 데이터 순서 안바뀜 이 방법을 추천
a_gpu = gpuarray.to_gpu(np.asanyarray(a_cpu,order='F'))

# create empty gpu array for the result (C = A * B)
#c_gpu = gpuarray.empty((MATRIX_SIZE, MATRIX_SIZE), np.float32)
c_gpu = gpuarray.empty_like(a_gpu)

# get the kernel code from the template
# by specifying the constant MATRIX_SIZE
kernel_code = kernel_code_template % {
    'size_x': MATRIX_SIZE_x, 'size_y': MATRIX_SIZE_y}

# compile the kernel code
mod = compiler.SourceModule(kernel_code)

# get the kernel function from the compiled module
matrixmul = mod.get_function("mycuCopy")

# call the kernel on the card
#%timeit matrixmul(a_gpu, b_gpu,c_gpu,block = (8, 8, 1))

blocksize=(2,3,1)
matrixsize=(MATRIX_SIZE_x,MATRIX_SIZE_y,1)
gridsize=tuple(int((matrixsize[i]+blocksize[i]-1)/blocksize[i]) for i in range(3))

matrixmul(c_gpu, a_gpu,
block = blocksize, grid=gridsize)

# print the results
print ("-" * 80)
print ("Matrix A (GPU):")
print (a_gpu.get())

print ("-" * 80)
print ("Matrix C (GPU):")
print (c_gpu.get())

print ("-" * 80)
print ("CPU-GPU difference:")
print (c_cpu - c_gpu.get())

print(np.allclose(c_cpu, c_gpu.get()))
