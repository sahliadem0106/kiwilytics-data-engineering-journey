import numpy as np
x1=np.array([[1,2,3],[4,5,6]])
print(x1,"\n")
x2=x1  #in this case x2 gets the pointer of x1 and points to the same array i didnt copy the array and get a second x1 named x2 in another place in the memory 
x2[0,2]=9
print(x1,"\n\n",x2,"\n")
#-----------------------
y1=np.array([[1,2,3],[4,5,6]])
print(y1,"\n")
y2=y1.copy()  # in this case we copied y1 to y2 and we haev two seperate tables , this shows that we need copy()  to copy a table not "   =   "
y2[0,2]=9
print(y1,"\n\n",y2,"\n")
#arithmatics : 
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("arr","\n",arr+5,"\n")
print("arr","\n",arr-5,"\n")
print("arr","\n",arr*5,"\n")      #operation on an array will be applied on every elemnts and value
print("arr","\n",arr/5,"\n")
print("arr","\n",arr**5,"\n")