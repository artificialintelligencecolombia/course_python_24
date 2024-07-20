#!/usr/bin/env python3

import pandas as pd

# -> EXPLORE THE DATASET

# Specify the file path
FILE_PATH = './central_park_squirrel_data.csv'

# Read the csv file into a DataFrame
df = pd.read_csv(FILE_PATH)

# -> ANALYZE THE DATA

# Count for the missing values in the primary fur color column
missing_fur_color_total = df['Primary Fur Color'].isnull().sum()

# Count the values
fur_color_counts = df['Primary Fur Color'].value_counts()

# export the results to a CSV file
fur_color_counts.to_csv('./fur_color_counts.csv')

# -> PRINT THE RESULTS
print(fur_color_counts)
print('Empty rows: ', missing_fur_color_total)
print('\nNumber of records: ',df.shape[0])
