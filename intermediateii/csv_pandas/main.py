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
filtered_df = df.dropna(how='all')

# -> Filter out rows that contain the word total in any column
filtered_df = filtered_df[
    ~filtered_df.apply(lambda row: row.astype(str).str.contains('total').any(), axis=1) 
]
# df.apply(lambda ,axis=1) -> the function should be applied to each row
# lambda row: -> Take row as argument.
# row.astype(str) -> Convert the row obj to a string
# str.contains('total') # Checks each string element in the row to see if it contains the substring 'total'. returns Boolean
# any() -> Checks all the cells of the row
# Without '~' -> finds and returns the row with 'total'.
# With '~' -> finds and returns all rows, except 'total'.

print(f"Filtered Dataframe: \n {filtered_df}")

# -> Convert the df to a list
rows = filtered_df.values.tolist()

# -> Create a list with the names of the inventory
chemicals = []
for row in rows:
    chemicals.append(row[1])

print(chemicals)
print(filtered_df['insumo'])