#!/usr/bin/env python3

# -> Import pandas library
import pandas as pd

# -> Specify the file path
FILE_PATH = './inventarios_living_antioquia - inventarios_jul.csv'

# -> Read the .csv file into a dataframe -> Skip the first row
df = pd.read_csv(FILE_PATH, skiprows=1)

# -> Filter out empty rows
filtered_df = df.dropna(how='all') # drop rows only if all columns in that row contain NaN values

# -> Filter out rows that contain the word total in any column
filtered_df = filtered_df[
    ~filtered_df.apply(lambda row: row.astype(str).str.contains('total').any(), axis=1) 
]
print(f'Filtered DataFrame: \n',filtered_df)

# Clean the column 'costo_unitario_iva_inc'
costo_unitario_col = filtered_df['costo_unitario_iva_inc'].replace('[\$,\s]', '', regex=True) # Removes $, commas, and spaces from the column using regex

# Converts cleaned strings to numbers, changing non-numeric values to NaN
costo_unitario_col = pd.to_numeric(costo_unitario_col, errors='coerce') # errors='coerce' -> invalid parsing will be set as NaN (Not a Number)

# Calculate the average by computing the mean of the col
costo_unitario_avg = costo_unitario_col.mean()

print('Columna costo_unitario_iva_inc: \n', costo_unitario_col)
print(f'The average unitary cost is: {costo_unitario_avg}')
