#!usr/bin/env python3
# Open the inventarios.csv, read it and create a list named 'data' that contains the values from the .csv file

# -> Import pandas library
import pandas as pd

# -> Specify the file path
FILE_PATH = './inventarios_living_antioquia - inventarios_jul.csv'

# -> Initialize the list to store rows
rows = []

# -> Read the .csv file into a dataframe -> Skip the first row
df = pd.read_csv(FILE_PATH, skiprows=1)

# -> Filter out empty rows
filtered_df = df.dropna(how='all') # drop rows only if all columns in that row contain NaN values

# -> Filter out rows that contain the word total in any column
filtered_df = filtered_df[
    ~filtered_df.apply(lambda row: row.astype(str).str.contains('total').any(), axis=1) 
]
# filtered_df.apply(lambda ,axis=1) -> the function should be applied to each row of the dframe. Function should be applied row-wise.
# lambda row: -> Anonymous fn, take row as argument.
# row.astype(str) -> Convert the row obj to a string
# str.contains('total') # Checks each string element in the row to see if it contains the substring 'total'. returns Boolean
# any() -> Returns True if any element in the Boolean series is True.Effectively checks if 'total' appears in any column of the row.
# Without tilde'~' -> finds and returns the row with 'total'.
# With '~' -> finds and returns all rows, except 'total'.

print(f"Filtered Dataframe: \n {filtered_df}")

# -> Convert the df to a list
rows = filtered_df.values.tolist()

# -> Create a list with the names of the inventory
chemicals = []
for row in rows:
    chemicals.append(row[1])

print(f'List_of_chemicals: \n',chemicals)
print('\n',type(filtered_df['insumo']),filtered_df['insumo'])

# Create a list from a data series
list_from_series = filtered_df['insumo'].tolist()
print('\nList of chemicals: ',list_from_series)

# Calculate an average value from a Data Series (column)
costo_unitario_avg = filtered_df['costo_unitario_iva_inc'].mean()
print(type(costo_unitario_avg))
print(f"Average costo unitario: \n",costo_unitario_avg)