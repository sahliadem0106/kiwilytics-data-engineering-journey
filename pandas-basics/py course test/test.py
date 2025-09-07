import pandas as pd

#load csv file
df=pd.read_csv("py test/kiwilytics_orders.csv")
print(df.head(100))
print(df.info())
print(df.isna().sum)
prod_avg_price=df.groupby("product")['unit_price'].mean()
print(prod_avg_price)
df["unit_price"]=df["unit_price"].fillna(df['product'].map(prod_avg_price)) 
print(df.head(100))    #When we use df['product'].map(prod_avg_price), it searches for each value in the df['product'] Series (e.g., "Kiwi Candy", "Kiwi Chips", etc.) within the index of the prod_avg_price Series and returns the corresponding value from prod_avg_price.  // General Behavior: The map() method in pandas (when used with a Series as the argument) performs a lookup operation. It takes each value in the calling Series (the one you call map() on) and uses it as a key to find a corresponding value in the index of the provided Series.
print(df.isna().sum)
total_revenue=(df["unit_price"]*df["quantity"]).sum()
print(total_revenue)
sum_Q_for_products=df.groupby("product")['quantity'].sum()
print(sum_Q_for_products)
df["money_spent"]=df['quantity']*df['unit_price']
sum_SM_for_clients=df.groupby("customer_name")['money_spent'].sum().sort_values(ascending=False)
print(sum_SM_for_clients)