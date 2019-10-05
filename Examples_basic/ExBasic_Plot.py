# inital importation
import matplotlib.pyplot as plt
import numpy as np
import math

# %matplotlib qt
# %matplotlib inline

# <codecell> print test
print("hello 한글")

# In[]: subplot test
t=np.linspace(0,20,400)

fig1 = plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t, np.sin(t)); plt.title('1st subplot')
plt.subplot(2,2,2); plt.title('2nd subplot')
plt.plot(t, np.cos(t))
plt.show()
# fig1.savefig('ExBasic_Plot_result.png')

# sqrt test
a=3; b=2
c=math.sqrt(9)*a**b
print(c)

# In[]: multiple plot test
fig2 = plt.figure(2)
plt.plot(np.sin(t))
plt.plot(np.cos(t))
plt.xlim(1, 500); plt.title('sin and cos');plt.legend(['sin','cos'])
plt.show()
plt.clf()
