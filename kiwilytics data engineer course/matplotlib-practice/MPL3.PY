from matplotlib import pyplot as plt
import numpy as np
A=[10,11,12,13,14,15,16]
B1=[100,170,200,270,300,370,400]    #place 1
B2=[90,110,130,150,170,190,210]     #place 2
plt.plot(A,B1,color='red',linestyle='-.',marker='x',label='GRAPH 1')
plt.plot(A,B2,color='blue',linestyle='--',marker='o',label='GRAPH 2')
plt.title('styled one')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True)
plt.show()
#look we defined the label when we made the plot w also can define it with the legend "explicit legend"
#also instead of wasting time styling we can see available styles  with printing(plt.style.available) they we use it using plt.style.use('choosen style')

