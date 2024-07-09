# Create a dataset related to the sales of a fictional retail store.
# Columns: OrderID,Product,Category,Quantity,Price,TotalPrice,OrderDate

# import libraries
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta 

# Define the number of rows
num_rows = 100

# Generate OrderID in list format
order_ids = list(range(1, num_rows + 1)) # 1 - 100
# print(order_ids)

# Define possible products and categories
products = ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E', 'Widget F', 'Widget G', 'Widget H', 'Widget I', 'Widget J', 'Widget K']
categories = ['Electronics', 'Home Goods', 'Clothing', 'Furniture']

# List comprehension

# Generate random products and categories
product_list = [random.choice(products) for _ in range(num_rows)]
categories_list = [random.choice(categories) for _ in range(num_rows)]
# [expression for item in iterable]

# Generate random quantities and prices
quantity_list = [random.randint(1,10) for _ in range(num_rows)]
prices_list = [round(random.uniform(5.00, 50.00), 2) for _ in range(num_rows)]
# print(prices_list)

# Calculate the total price for each record
total_price_list = [round(quantity_list[i] * prices_list[i], 2) for i in range(num_rows)]

# Generate the random order dates
start_date = datetime(2020,3,25) # init day
today = datetime.today() # gets current date    
delta_days = (today - start_date).days # number of days from start date to today
print(delta_days)

# Generate a list of random order dates within the range from start_date to today.
# For each of the num_rows (number of rows specified):
# - Generate a random number of days between 0 and delta_days.
# - Create a new date by adding this random number of days to start_date.
# - Format the new date as a string in the format 'YYYY-MM-DD'.
order_date_list = [(start_date + timedelta(days=random.randint(0,delta_days))).strftime('%Y-%m-%d') for _ in range(num_rows)]

# Create DataFrame
data = {
    'OrderID': order_ids,
    'Product': product_list,
    'Category': categories_list,
    'Quantity': quantity_list,
    'Price': prices_list,
    'TotalPrice': total_price_list,
    'OrderDate': order_date_list
}
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('retail_store_sales/sale_data.csv', index=False)
print("CSV file 'sales_data.csv' created successfully.")