 #we will learn repeating and stacking array
import numpy as np   
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("arr","\n",arr,"\n")
arr1=np.repeat(arr,2)      # witohut mentioning the axe to work on he will make the array flat (flatenned) mais repeated  and in the same time he will repeat  values so next time we wil mention the axe that we will work on 
print("arr","\n",arr1,"\n")
arr2=np.repeat(arr,2,axis=0)  #axis=0    ===> rows
print("arr","\n",arr2,"\n")
arr3=np.repeat(arr,2,axis=1)  #axis=1    ===> cols
print("arr","\n",arr3,"\n")
print("\n\n\n\n\n\n\n\n\n")
# we will learn how to stack arrays

a=np.array([1,2,3,4])
print(a,"\n")
b=np.array([5,6,7,8])
print(b,"\n")   #stacking , vertical and horyzantal , put them near each other
#vertical stack is made by calling vstack from numpy "np" also we need to pick the order of the stacking 
print("vertical stacking :","\n",np.vstack([a,b,a,b]),"\n")     # you can chooose any array to stack 
#horizontal stack is made by calling hstakc from numpy "np" also we need to pick the order o fthe stacking
print("horizontal stacking  : ","\n",np.hstack([a,b,a,b]),"\n\n")
print("\n\n\n\n")


#we will learn how to concatinate arrays 
k=np.array([[1,2,3,4],[5,6,7,8]])
print(k,"\n\n")
k1=np.array([[9,10,11,12],[13,14,15,16]])
print(k1,"\n\n")
# time to concatinate  we need to mention in parametre what arrays we are going to concatinate and then the axis
print("first concatination \n",np.concatenate((k,k1),axis=0),"\n")  # row=0 (on top)  
print("second concatenation\n",np.concatenate((k,k1),axis=1),"\n")   #column =1  coolumn beside  
print("\n\n\n\n")
print("\n\n\n\n")  



#array manipulattion : (generate , reshape and transpose arrays)
#np.arange(start,end,number of steps) creates array , end is not included
x=np.arange(0,9,2)
print(x,"\n\n")
#np.linspace(start,end,number of samples) creates evenly spaced samples
y=np.linspace(1,100,10)
print(y,"\n\n")
arr=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(arr,"\n\n")
#arr.reshape(rows,cols) changes the array size ( before 7*2=14, after must equal 14)
print("reshaped arr",arr.reshape(7,2))    ##its not  transpose
#np.transpose(arr)  ====> rows = columns & columns = rows 
print("transposed arr \n",np.transpose(arr))
#to falt an array we sue .flat[:]
print("flattened array",arr.flat[:])      