#!usr/bin/env python3

import pandas as pd

# -> DATA COLLECTION & CLEANING

# Define the path of the file as constant
FILEPATH = './inventory_chemistry_company_jul.csv'

# -> Read the .csv file into a dataframe -> Skip the final rows (empty, total)
df = pd.read_csv(FILEPATH, skiprows=1, skipfooter=2, engine='python')

pd.set_option('display.width', None)  # Additional feature: Auto-detect the width of the display

# Filter out empty rows where all elements are NaN
df_fil1 = df.dropna(how='all')

# Drop columns with all missing values
df_fil2 = df.dropna(how='all', axis=1)

# Drop duplicates
df_fil3 = df.drop_duplicates()

# Set the columns to convert its data types
date_columns = ['fecha', 'purchase_date', 'production_date']
currency_columns = ['costo_unitario_iva_inc','costo_total']

# Convert data types for datetime
for col in date_columns:
    df_fil3[col] =pd.to_datetime(df_fil3[col], format='%m/%d/%Y')

print(f"df: {df_fil3}") # out: type pandas.DataFrame
    
# Convert data types for currency
def convert_currency(value):
    # Check if the value is already a float
    if isinstance(value, float) or isinstance(value, int):
        return value
    # Remove '$' ',' and leading and trailing whitespaces
    return float(value.replace('$','').replace(',','').strip())
for col in currency_columns:
    df_fil3[col] = df_fil3[col].apply(convert_currency)


print(f"df.shape: {df_fil2.shape}")