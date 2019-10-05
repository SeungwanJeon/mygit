import numpy as np

a=np.array([1,2,3,4])
print(a)
print(type(a),a.ndim,a.shape)

b=np.array([[1,2,3],[4,5,6]])
print(b)
print(type(a),b.ndim,b.shape)

c=np.array([[1],[2],[3]])
print(c)
print(type(a),c.ndim,c.shape)

print(np.reshape(a,[-1,1]))

a=np.random.rand(2,2)
a.astype(int)


a=np.array([1,2,3])
print(type(a),end='\n\n')
print(a.shape, end='\n\n')
print(a[0],a[1],a[2],end='\n\n')
a[0]=5
print(a)

c=np.full((2,2),7)
print(c)

d=np.eye(2)
print(d)


np.random.random(5)
np.random.rand(5)

np.random.randn(3,2)
np.random.bytes(1)
np.random.randint(3,size=(2,3))


a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:3]
print(b)
b[0,0]=77
print(a)

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a[:2,1:3].copy()
print(b)
b[0,0]=77
print(a)

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=np.array(a[:2,1:3])
print(b)
b[0,0]=77
print(a)

a[1,:]
a[1:2,:]
a[1,:]*a[1:2,:]

a=np.random.rand(1024,512)
b=np.random.rand(1024,512)
c=np.random.rand(512,1024)

a*b
%timeit np.dot(a,c)
%timeit np.matmul(a,c)
%timeit a@c

%timeit np.dot(a,c)
%timeit np.matmul(a,c)
%timeit a@c



a
a[[0,1,2],[0,1,1]]
a[range(3),[0,1,1]]
a[:,[0,1,1]]
a.dtype
a.astype(np.float16).dtype
np.random.rand(2,1).astype(np.float16)*100


a=np.random.rand(2,3)
b=np.random.rand(2,3)
np.sum(a,axis=1)
np.sum(a,axis=1,keepdims=1)
a.max()
np.max(a,0)
np.maximum(a,0.5)
a
np.expand_dims(a,axis=2).shape








x=np.random.rand(2,3).astype(np.float16)
v=np.array([1,1,1]).astype(np.float16)
y=np.empty_like(x)
for i in range(x.shape[0]):
    y[i,:]=x[i,:]+v
print(y)
vv=np.tile(v,(x.shape[0],1))
print(x+vv)

print(x+v)


x=np.random.rand(3,1).astype(np.float16)
np.sqrt(x.T**2+x**2)


y=np.array([15,25]).reshape(-1,1)
W=np.array([[1,1],[2,1]])
x=np.linalg.inv(W)@y
print(x)


np.array(['2.3',2])


id(1.2000)
id(1+0.2)
int('11',2)
int('a1',16)
len((1,'ab'))


a=[4,2,3]
b=list(a)
id(a)
id(b)

list(map(lambda x:x+1,[1,2,3]))
list(map(str,[1,2,3]))

sorted(a)
