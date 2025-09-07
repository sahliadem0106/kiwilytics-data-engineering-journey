#LETS PLOT 2 GARPHS ON THE SAME CHART
from matplotlib import pyplot as plt
import numpy as np
A=[10,11,12,13,14,15,16]
B1=[100,170,200,270,300,370,400]    #place 1
B2=[90,110,130,150,170,190,210]     #place 2
plt.plot(A,B1)
plt.plot(A,B2)
plt.title("second graph")
plt.xlabel("size (m2)")
plt.ylabel("price (kusd)")
#to know which one is 1 or 2  ,we need to add legend , a legend will define each graph 
plt.legend(['GRAPH 1','GRAPH 2'])
plt.show()
#lets put some styling to make it more clear my G , its not our duty but we need to make a plot that makes us understand more our data , missing cases , etc , its for better wrangling
#go MPL3.PY