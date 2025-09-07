#append and append array to another
import numpy as np
u=np.array([[1,2,3,4],[5,6,7,8]])
print("u","\n",u,"\n")
u1=np.append(u,[[9,10,11,12]],axis=0)
print("u1","\n",u1,"\n")
u2=np.append(u,[[5],[9]],axis=1)
print("u2","\n",u2,"\n")
#insert which is appending but with choosing the place of the new row/col , deletetion
r=np.array([[1,2,3,4],[5,6,7,8]])
print("r","\n",r,"\n\n\n")
r1=np.insert(r,2,[[11,12,13,14]],axis=0)
print("r1","\n",r1,"\n")
r2=np.insert(r,3,[10,11],axis=1)
print("r2","\n",r2,"\n")
r3=np.delete(r,1,axis=1)
print("r3","\n",r3,"\n")
#----------------------------
# create an array from an existing array  using numpy
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print(a)
x=a[2:4,0:2]      # x  db:fin   ,   y   db:fin 
print(x)

