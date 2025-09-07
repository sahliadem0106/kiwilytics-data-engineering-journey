# in RWDWP.py we cleaned and exported data in the end lets use it

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#visulization 1 : top countries by shipping cost
plt.figure(figsize=(10,5))    #This creates a new figure (a canvas for my plot) with a specified size. The figsize parameter takes a tuple (width, height) in inches, so (10, 5) sets the figure to 10 inches wide and 5 inches tall.  

df=pd.read_csv("real-world data wrangling problem ( with pandas )/cleane orders final.csv")
print(df.head())
#csv file do not keep each column type so we need to convert the date again 
df['OrderDate']=pd.to_datetime(df['OrderDate'])
df['ShippedDate']=pd.to_datetime(df['ShippedDate'])
#now lets visualize :
df.groupby("ShipCountry")['ShippingCost'].mean().sort_values().plot(kind="barh",color="blue")
plt.title("avg shipping cost by country")
plt.xlabel("avg shipping cost")
plt.ylabel("country")
plt.grid(True)
#lets adjust the layout to prevent label cutoff
plt.tight_layout()     #This function automatically adjusts the spacing between subplots and the figure edges to prevent overlapping of labels, titles, or tick marks. It optimizes the layout so that all elements fit nicely within the figure area
##we need to go back to the top to change the plot size 
plt.show()
#-----------------------------
#visulization 2 : delivery days distribution , how much delivery per day 
plt.figure(figsize=(10,5))
df['DeliveryDays'].dropna().plot(kind='hist',bins=30,color="skyblue",edgecolor="black")   #it looks like a signal , not clear at all lets add
plt.title("distribution of deliverry days")
plt.xlabel("delivary days")
plt.ylabel("frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
#visulization 3 : delivery status count  pie charts
df["DeliveryStatus"].value_counts().plot(kind="pie",colors=["#EA3216","grey","green"])
plt.title("delivery status count")
plt.ylabel("")
plt.show()
#visulization 4 : Monthly Order Volume
df['Months']=df["OrderDate"].dt.to_period("M")  
monthly_order=df.groupby('Months').size()   # or count()  ..... more explanation : The size() method, when applied after groupby(), counts the number of rows (or entries) in each group, regardless of whether there are missing values (NaN). It returns a Series where the index is the unique group labels (e.g., the months), and the values are the counts of rows in each group.
#This is different from .count(), which counts non-null values in each column of the group. size() simply gives the total number of rows per group, including NaN if present.   so this is a date and the database is clean so there is nothing with using count guess
plt.figure(figsize=(12,6))
monthly_order.plot(kind="line",marker='o',color='yellow')
plt.title("Monthly Order Volume")
plt.xlabel("month in every year")
plt.ylabel("order volume")
plt.grid(True)
plt.tight_layout()
plt.show()

