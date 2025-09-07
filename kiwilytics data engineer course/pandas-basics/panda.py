import numpy as np
import pandas as pd
#series
monthly_revenue=pd.Series([30000,50000,45000,np.nan,60000], name="revenue")
print("monthly revenue series:\n",monthly_revenue,"\n")
#dataframe: employees at different firms
data = {
    'employee':['adem','louay','aziz','maher'],
    'company' :['kaust','pwc','amazon','jazira'],
    'expy' : [5,7,3,9]
}
df=pd.DataFrame(data)
print("data frame \n",df)
#----------------------------
#Explore and Inspect your dataframe
print("first 5 rows \n")
print(df.head())    #  .head() shows first 5  , u can choose the number and change it in the head function parametre
print("last 5 rows\n")
print(df.tail(1))     #  .tail() show slast  5 ,  u can choose the number and change it in the tail function parametre
# we use head and tail to view last , first rows in a dataframe
#----------------------------------
# info summary about the dataframe      we use info()
print("dataframe info \n")
df.info()
# dataframe desciption , shows min , max     we use describe()
print("summary statistics:")
print(df.describe(),"\n\n")
#lets cheack if there is some nulls 
print(df.isna().sum())     #shows how much nulls in each column (NullExistingSummary)
#view full matrix of missing positions
print(df.isna())
#----------------------------------
#simulate a missing experience value
df.loc[2,'expy']=np.nan      # in this case i putted : to switch all data in columns expy to NaN    df.loc  locate a specific row if i use only the index or an  element in that row if i use index + column name, and give  access to it to change value 
print("data frame \n\n\n",df)
#lets cheack again if there is some nulls 
print(df.isna().sum())     #it will show 4 
#now lets say that we dont need to see any row in the data frame that have a NaNs in it (missing data) , lets say we dont need it 
#we use df.dropna() to drop rows with missing data
print(df.dropna())
#reset & re-initialze the dataframe to its original clean state :
data = {
    'employee':['adem','louay','aziz','maher'],
    'company' :['kaust','pwc','amazon','jazira'],
    'expy' : [5,7,3,9]
}
df=pd.DataFrame(data)
print("data frame \n",df)
## now in real life cases we will have a lot of columns to work with and also sometime i will need to see only one so lets see how can i do it:
#to select a specific column we print df['column_name']
print("company names :\n",df['company'],'\n\n')
#to select a group of columns we print df[['column1','column2',' ']]   (  [['c1','c2','cn']])
print("company names and expy :\n",df[['company','expy']],'\n\n')
#to select a specific row that we know his index we print df.loc[index,column] or df.loc[index]]
print(" row by index \n",df.loc[2],"\n\n")  #index is a number in this case and not a letter or a label
#to select a specific row that we know his position (row, column) we print df.iloc
print("row by position\n",df.iloc[1],"\n\n")    #index is a number in this case
#lets explain and show more use cases about loc and iloc (using ai :3 )
### **Key Differences**

###1. **Indexing Type**:
###   - **`loc`**: Uses **label-based indexing**. You select data using row and column labels (e.g., index names or column names).
###   - **`iloc`**: Uses **integer-based indexing**. You select data using numerical positions (zero-based, starting from 0).

###2. **Inclusivity in Slicing**:
###   - **`loc`**: Includes the end label in a slice (inclusive).
###   - **`iloc`**: Excludes the end position in a slice (exclusive, like standard Python slicing).

###3. **Use Cases**:
###   - Use `loc` when working with labeled indices or column names.
###   - Use `iloc` when you need to access data by numerical positions, especially with numeric or non-standard indices.

###4. **Error Handling**:
###   - **`loc`**: Raises a `KeyError` if a label doesn’t exist.
###   - **`iloc`**: Raises an `IndexError` if a position is out of bounds.

### **Syntax**
###     **`loc`**: `df.loc[row_labels, column_labels]`
###     **`iloc`**: `df.iloc[row_positions, column_positions]`

#---------------------------------


# Sample DataFrame creation
# data = {
#     'A': [1, 2, 3, 4],
#     'B': [10, 20, 30, 40],
#     'C': [100, 200, 300, 400]
# }
# df = pd.DataFrame(data, index=['w', 'x', 'y', 'z'])
# print(df)
# Output:
#    A   B    C
# w  1  10  100
# x  2  20  200
# y  3  30  300
# z  4  40  400

# Example 1: Selecting a Single Value

# Using loc:
# # Get value at row label 'x' and column 'B'
# value = df.loc['x', 'B']
# print(value)
# Output: 20

# Using iloc:
# # Get value at row position 1, column position 1
# value = df.iloc[1, 1]
# print(value)
# Output: 20
# Explanation: loc uses the label 'x' and column name 'B', while iloc uses the integer positions 1 for both row and column.


#---------------------------------------------



# Example 2: Slicing Rows and Columns

# Using loc:
# # Select rows 'w' to 'y' and columns 'A' to 'B'
# slice_loc = df.loc['w':'y', 'A':'B']
# print(slice_loc)
# Output:
#    A   B
# w  1  10
# x  2  20
# y  3  30

# Using iloc:
# # Select rows 0 to 2 and columns 0 to 1
# slice_iloc = df.iloc[0:3, 0:2]
# print(slice_iloc)
# Output:
#    A   B
# w  1  10
# x  2  20
# y  3  30
# Explanation: loc includes the end label ('y'), while iloc excludes the end position (3). Both methods produce the same result here because the slice aligns with the positions and labels.


#---------------------------------------------


# Example 3: Selecting Specific Rows and Columns

# Using loc:
# # Select rows 'x' and 'z' for column 'C'
# subset_loc = df.loc[['x', 'z'], 'C']
# print(subset_loc)
# Output:
# x    200
# z    400
# Name: C, dtype: int64

# Using iloc:
# # Select rows at positions 1 and 3 for column position 2
# subset_iloc = df.iloc[[1, 3], 2]
# print(subset_iloc)
# Output:
# x    200
# z    400
# Name: C, dtype: int64
# Explanation: loc uses explicit labels ('x', 'z', 'C'), while iloc uses their corresponding positions (1, 3, 2).

#-------------------------------


# Example 4: Modifying Values

# Using loc:
# # Modify value at row 'y', column 'A'
# df.loc['y', 'A'] = 99
# print(df)
# Output:
#    A   B    C
# w  1  10  100
# x  2  20  200
# y 99  30  300
# z  4  40  400

# Using iloc:
# # Modify value at row position 2, column position 0
# df.iloc[2, 0] = 3
# print(df)
# Output:
#    A   B    C
# w  1  10  100
# x  2  20  200
# y  3  30  300
# z  4  40  400
# Explanation: Both methods can modify values, but loc uses labels, and iloc uses positions.

# When to Use loc vs. iloc

# Use loc:
# - When you know the index or column labels.
# - When working with non-numeric or custom indices (e.g., strings like 'w', 'x').
# - When you need inclusive slicing with labels.

# Use iloc:
# - When you need to access data by numerical position.
# - When the index is numeric or you don’t care about labels.
# - When working with dynamically generated DataFrames where labels are unknown.

#---------------------------
#Filtering 
#employees with more than 5 years of exp
print("employees with more that 5 years of experience :\n\n",df[ df['expy'] > 5 ],"\n\n")
#                                                                  |
#                                                                  |_____________________->   this is the filter , specify what data you want to see and filter and then apply it in the dataframe
#employee who work in pwc 
print("employee who work in pwc",df[df['company']=='pwc'])
# as a data engineer , sometimes we deal with datasets not standard,for exemple tunisia can be written in french arabic , lowercase and uppercase , this is frustrating for a data engineer so he need to make them all look the same ... HOW ?
#we standardize columns
#lets say we want all company name in uppercase , so those who works in Pwc & PWC both count
df['company']=df['company'].str.upper()   #simple exemple
print("data frame \n",df)
#lets add a new column to our dataframe
df['Is_Very_Senior']=df['expy'] >= 7    #we are making a column based  on a comparisation
print("data frame \n",df)
#in previous steps and lines we explored how to deal with null values , how to explore then and show our dataframe without rows with null values and instead of dropping them , we will replace them with min values vause sometimes i need to show all values , why min ? , bcs it will not affect the data that much (semi-realistic)  this exemple is known when we deal with a product review , so insead of putting 0 star for exemple we can put min review ( the prodcut is not that bad tho ) its not good to show people that the product is bad bcs of a bug that accept corrupted/missing data about reviews
df_projects=pd.DataFrame({
    'client': ['kaust','pwc','amazon','jazira'],
    'Budget_kUSD':[120,200,np.nan,150]
})
print("original budgets\n:",df_projects,"\n\n")
mean_budget=df_projects['Budget_kUSD'].mean()
print(mean_budget)
#now we created the mean budget , we need to replace every NaN with that , we use fillna(variable,value)
df_projects['Budget_kUSD']=df_projects['Budget_kUSD'].fillna(mean_budget)
print("after filling missing budgets \n:",df_projects,"\n\n")
#GROUPING AGGREGATING DATAFRAMES
# Revenue per company per quarter
df_revenue = pd.DataFrame({
    'Company': ['Kiwilytics', 'PwC', 'EY', 'KPMG', 'Kiwilytics', 'PwC'],
    'Quarter': ['Q1', 'Q1', 'Q1', 'Q1', 'Q2', 'Q2'],
    'Revenue_kUSD': [120, 200, 180, 150, 130, 210]
})
print(df_revenue,"\n\n\n")
grouped= df_revenue.groupby('Company')['Revenue_kUSD'].sum()     #grouped got a dataframe that have sum of revenues for every company so its showing sum of revenues grouped by company name
print("total revenue by company\n",grouped,"\n")
#MERGING DATAFRAMES 
#  we are going to merge project managers and projects , lets create project manager dataframe  ( its like joins in sql)
df_managers = pd.DataFrame({
    'ManagerID': [1, 2, 3],
    'Name': ['Ibrahim', 'Maher', 'Abdelrahman']
})

print(df_managers)

df_projects = pd.DataFrame({
    'ProjectID': [101, 102, 103],
    'ManagerID': [1, 2, 2],
    'Client': ['Kiwilytics', 'PwC', 'EV']
})

print(df_projects)
#column name that we will use to merge the two dataframes should be same in this case ManagerID
merged_df=pd.merge(df_managers,df_projects,on='ManagerID',how='inner')     # pd merge need at least two dataframes to merge , on what column , and type of merging ( inner join , left , right , full outer)

print(merged_df)