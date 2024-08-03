#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -> DATA COLLECTION & CLEANING

# Define the path of the file as constant
FILEPATH = './inventory_chemistry_company_jul.csv'

# Read the .csv file into a dataframe -> Skip the final rows (empty, total)
df = pd.read_csv(FILEPATH, skiprows=1, skipfooter=2)

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Filter out empty rows where all elements are NaN
df = df.dropna(how='all')

# Drop columns with all missing values
df = df.dropna(how='all', axis=1)

# Drop duplicates
df = df.drop_duplicates()

pd.set_option('display.width', None)  # Additional feature: Auto-detect the width of the display

# Check and convert date columns
date_columns = ['fecha', 'purchase_date', 'production_date']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], format='%m/%d/%Y', errors='coerce')
    
# Check and convert currency columns
currency_columns = ['costo_unitario_iva_inc','costo_total']

def clean_currency(value):
    if isinstance(value, str): # checks if 'value' is a string
        value = value.strip().replace('$', '').replace(',', '').replace(' ', '') # removes leading and trailing spaces | removes '$' ',' and ' '
        if value == '' or value == '-': 
            return 0
        try: # attempt to convert the cleaned str to a float
            return float(value) # return cleaned value, float format
        except ValueError:
            return None
    return value # if not a str -> return it as-is.

for col in currency_columns: # For each column in the list of currency columns ...
    df[col] = df[col].apply(clean_currency) # ... apply clean_currency to each element of the column

# TEST: export the results to a CSV file for checking the cleaning
df.to_csv('./cleaned_data.csv')

print(df)

# -> VISUALIZATION

# 1. Box Plot for Cost Distributions: Visualize the spread and outliers in the costo_unitario_iva_inc and costo_total columns.
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['costo_unitario_iva_inc'])
plt.title('Box Plot of costo_unitario_iva_inc')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['costo_total'])
plt.title('Box Plot of costo_total')

plt.tight_layout()
plt.show()

# 2. Bar Plot for Categorical Data: Show the frequency of different categories in tipo, primary_units, and proveedor_1.
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
sns.countplot(y=df['tipo'])
plt.title('Counts of Tipo')

plt.subplot(1, 3, 2)
sns.countplot(y=df['primary_units'])
plt.title('Counts of Primary Units')

plt.subplot(1, 3, 3)
sns.countplot(y=df['proveedor_1'])
plt.title('Counts of Proveedor 1')

plt.tight_layout()
plt.show()

# 3. Pair Plot: Visualize the pairwise relationships between numerical variables, including cantidad, costo_unitario_iva_inc, and costo_total.
sns.pairplot(df, vars=['cantidad', 'costo_unitario_iva_inc', 'costo_total'])
plt.show()

# 4. Box Plot by Category: Compare the distribution of costo_total for different categories in tipo.
plt.figure(figsize=(12, 6))
sns.boxplot(x='tipo', y='costo_total', data=df)
plt.title('Costo Total by Tipo')
plt.xticks(rotation=45)
plt.show()

# Topic: Data Cleaning vs Data Preprocessing

# Data Cleaning:
# - Focuses on detecting and correcting (or removing) corrupt or inaccurate records from a dataset.
# - Involves handling missing values, removing duplicates, correcting data types, handling invalid data, etc.

# Data Preprocessing:
# - A broader term that includes data cleaning but also involves transforming and organizing raw data into a format suitable for analysis.
# - Includes steps like data integration (combining data from multiple sources), data transformation (normalization, aggregation), feature engineering, encoding categorical variables, and scaling/normalizing numerical features.