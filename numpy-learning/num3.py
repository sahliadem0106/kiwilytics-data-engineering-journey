import numpy as np
a=np.zeros((2,3))   #matrice nulle
print(a,"\n")
b=np.ones((2,3))    # matrice de 1
print(b,"\n")
c=np.full((2,3),4)     #matrice fulll of a valuee string , float , number. )   
print(c,"\n")
d=np.identity(5)        #matrice i  5*5
print(d,"\n")
#---------------------------------------
#random matrics:
e=np.random.rand(2,3)
print(e,"\n")
f=np.random.randint(1,6,(2,3))    #debut,fin,size (x,y)   
print(f,"\n")