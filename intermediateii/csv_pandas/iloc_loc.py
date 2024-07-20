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

# Set 'insumo' (or appropriate column) as the index
filtered_df.set_index('insumo', inplace=True)

# Access the row with index 'cloruro de sodio'
try:
    row = filtered_df.loc['cloruro de sodio']
    print(row)
except KeyError:
    print("The index 'cloruro de sodio' does not exist in the DataFrame.")