import numpy as np
import pandas as pd
#to read the CSV file we need to use read_csv
df=pd.read_csv("real-world data wrangling problem ( with pandas )/orders_with_issues.csv")      #must be in the same directory 
print(df.head())
#lets make a summary
print(df.info())
#nulls and nans
print(df.isna().sum)
#lets cheack unique shipping companies , to know unique values in a column we use values
print(df['ShippingCompany'].value_counts())
#as a data engineer you need to play with these functions when u first get access to the dataset so u get info about what are you working with      LOADING & EXPLORATION THE DATASET
#now its time to clean data 
#in this process we think wisely and cheacks all values in the dataset and see what could make a problem for me or lets say a data scientist , dates , negative values , undefined data types ... and build a path for every one , if its case A we convert , if its case B We set data as NAT OR NAN etc you clean as much as u can (illogical data will be convertel to nulls and then we will deal with it )
#Convert dates
df['OrderDate']=pd.to_datetime(df['OrderDate'],errors='coerce')        #old OrderDate will get the new to datetime it self and in case of finding errors it will replaced with nulls
df['ShippedDate']=pd.to_datetime(df['ShippedDate'],errors='coerce')
#clean shipping cost
df['ShippingCost']=pd.to_numeric(df['ShippingCost'],errors='coerce')   #convert it to numeric and null strings and corrupted data
df.loc[df['ShippingCost'] < 0 , 'ShippingCost' ] =np.nan     #loc [rows  with shippingcost value <0 , shippingcost column ]    
#we cant let the nulls so we need to replace them in this case mean is not supper effective cause sometimes may be one or two shippingcost is so high and that will affect the mean to show a non realistic value so we are going to use median
df['ShippingCost']=df['ShippingCost'].fillna(df['ShippingCost'].median())
#we also should drop rows where both dates are missing if one is there and the other is not its okey
#methoo 1:
df=df[~(df['OrderDate'].isna() & df['ShippedDate'].isna())]     # the existing dataframe will be replaced with another dataframe that will only have rows that dont have orderdate and shippingdate both null
#or also i can drop rows instead of taking what i want 
df=df.drop(df[df['OrderDate'].isna() & df['ShippedDate'].isna()].index)
#now after setting some values to null we need to deal with every null if its a null in the data column ,or price or whatever 
#handling nulls , fixing fileds and standardization
#handling nulls decisions is mainly choosed from the client 
df['OrderID']=df['OrderID'].fillna(method='ffill')   ## flill it with the previous orderID (requested)
df['CustomerID']=df['CustomerID'].fillna("Unknonw")
df['ShipCity']=df['ShipCity'].fillna("Unspecified")
#standardize names
df['ShipCountry']=df['ShipCountry'].str.strip().str.title()
df['ShipCity']=df['ShipCity'].str.strip().str.title()
df['ShippingCompany']=df['ShippingCompany'].str.strip()
df.loc[df['ShippingCompany'].str.contains("Kiwilytics" ,na=False),'ShippingCompany']="Kiwilytics Goods Shipping LLC."
print(df.info())
print(df.isna().sum)
#everything is ready feature engineering : exporting fields , insights, first use case ( nb of late orders )
df['DeliveryDays']=(df['ShippedDate'] - df['OrderDate']).dt.days  
def get_status(x):
    if pd.isna(x):
        return "unknown"
    elif x > 15:
        return "late"
    else:
        return "shipped on time"
df['DeliveryStatus']=df['DeliveryDays'].apply(get_status)
print(df.head())
#now lets cheack if the delivery is domestic or no 
domestic_countries=["Germany"]
def cheack_domestic(country):
    if country in domestic_countries:
        return "yes"
    else:
        return "no"
df["isDomestic"]=df['ShipCountry'].apply(cheack_domestic)
print(df.head())
#grouping exemple 
avg_shippingcost_by_company=df.groupby("ShippingCompany")['ShippingCost'].mean()
print("AVG Simple Cost by Company :",avg_shippingcost_by_company)
#i guess after testing we need to export the new cleaned file we use  df.to_filetype("filename.type")
df.to_csv("cleane orders final.csv",index=False)  # we dont need indexes 
#lets see some data
print(df.head())
#delivary status  breakdown
print(df['DeliveryStatus'].value_counts())
#orders by country
print(df['ShipCountry'].value_counts())
#orders by city
print(df['ShipCity'].value_counts())
#top 3 shipping company
print(df['ShippingCompany'].value_counts().head(3))
# Alhamdulillah
#
# Key Takeaways:
#
# Exploratory Data Analysis
# - You learned how to inspect raw data, identify data quality issues, and understand column types, missing values, and distributions.
#
# Data Cleaning Techniques You practiced handling:
# - Invalid or missing dates
# - Non-numeric and negative values in cost fields
# - Nulls in critical columns like OrderID, CustomerID, and ShipCity
# - Inconsistent formatting and standardization
# - Feature Engineering
#
# You created new features like:
# - DeliveryDays: the number of days between order and shipment
# - DeliveryStatus: a flag for late vs on-time shipments
# - IsDomestic: to distinguish local vs international orders
# - Exporting Cleaned Data
#
# You prepared a final, cleaned dataset ready for analytics, reporting, or loading into a database.