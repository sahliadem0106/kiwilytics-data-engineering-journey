import numpy as np
#np.array creates an array
a = np.array([1,2,3])
print(a)
#a.ndim returns the dimension of the array 
print(a.ndim)
print(a.dtype)
#-----
#2D numpy array 
b=np.array([[1.1,2.4,3.3],[4.1,5.2,6.5]])
print(b)
#cheack dimension 
print(b.ndim)
#cheack shape x*x
print(b.shape)   # rows , columns
#data type
print(b.dtype)
