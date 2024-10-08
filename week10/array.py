import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(type(a))
print(a.shape)
b=np.zeros((2,2))
c=np.ones((2,2))
e=np.full((2,2),6)
f=np.random.random((2,2))
print(a)
print(b)
print(c)
print(e)
print(f)
print(b.dtype)
x=np.array([1,2], dtype=np.int64)
print(x.dtype)

x=np.array([[1,2],[3,4]], dtype=np.float64)
y=np.array([[5,6],[7,8]], dtype=np.float64)

print(x-y)
print(np.subtract(x,y))
print(np.multiply(x,y))
print(x.T)
print(np.sum(x))
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))
