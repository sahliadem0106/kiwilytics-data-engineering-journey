#plot a single graph:
from matplotlib import pyplot as plt
import numpy as np
#simple data
x=[10,11,12,13,14,15,16]
y=[100,170,200,270,300,370,400]
#basic line plot 
plt.plot(x,y)
plt.title("first graph")
plt.xlabel("size (m2)")
plt.ylabel("price (kusd)")
plt.show()
