import numpy as np

x = np.random.rand(256,256)

x_c=np.asanyarray(x, dtype=np.float32, order='C')
x_f=np.asanyarray(x, dtype=np.float32, order='F')

%timeit np.sum(x_c,axis=0)
%timeit np.sum(x_f,axis=0)

%timeit np.sum(x_c,axis=1)
%timeit np.sum(x_f,axis=1)



import tensorflow as tf


#Assume that the number of cores per socket in the machine is denoted as NUM_PARALLEL_EXEC_UNITS
#  when NUM_PARALLEL_EXEC_UNITS=0 the system chooses appropriate settings
NUM_PARALLEL_EXEC_UNITS=0
config = tf.ConfigProto(intra_op_parallelism_threads=NUM_PARALLEL_EXEC_UNITS,
                        inter_op_parallelism_threads=1,
                        allow_soft_placement=True,
                        device_count = {'CPU': NUM_PARALLEL_EXEC_UNITS})

session = tf.Session(config=config)

hello=tf.constant('abcdefg')
sess=tf.Session()
sess.run(hello)
print(str(sess.run(hello),encoding='utf-8'))
sess.close()
tf.__version__

import padas as pd
kk={'a':[1,2,3],'b':[2,3,4]}
print(kk)
