from scipy import io
import numpy as np

mat_file = io.loadmat('ExBasic_Load_mat_files_sample.mat')
data_a=np.array(mat_file['a'], dtype="float16")
data_b=mat_file['b']
data_b=data_b.astype("float32")

print(data_a)
print(data_b)
