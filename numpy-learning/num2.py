import numpy as np
c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],"\n")
print(c,"\n")
#print a specific column
print(c[1,2],"\n")   #this shows the value in row with index 1 ( number 2 ) and column with 2  (number 3)   
#print a row
print("second row:",c[1,:],"\n")    # : = all elements in a row
#print the last or - last row , the last row is -1 , the one before it is -2 wakeka
print("second to last row",c[-2,:],"\n")                                                            #: means all in case jet fel rows wela fel columns 
#print a column
print("third column",c[:,2],"\n")
#print the last or - last column , the last column is -1 , the one before it is -2 wakeka
print("last column ",c[:,-1],"\n")
#print a specific group in a line or a column 
print("the middle 2 elements in row 2",c[1,1:3])        #1:3   3 is excluded  
#if we want to update a value in the matrics wen can just decalare 
c[0,2]=20
print(c,"\n")
