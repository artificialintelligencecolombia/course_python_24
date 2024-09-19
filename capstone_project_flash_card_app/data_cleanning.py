import pandas as pd
import re

# Define the file path
FILE_PATH = './data/raw_data.csv'

# Load de CSV file
df = pd.read_csv(FILE_PATH)
# print("\nOriginal File: \n")
# print(df)

# Add header
header_list = ['russian']

# Conver the df to a csv
df.to_csv('./data/header_data.csv', header=header_list, index=False)

# Display the modified csv file
df2 = pd.read_csv('./data/header_data.csv')
#print(df_modi)

#Remove numbers and extra spaces
df2['russian'] = df2['russian'].apply(lambda x: re.sub(r'\d+','',x).strip())

# Save cleaned data
df2.to_csv('./data/cleaned_data.csv', index=False)

# Testing
#df_modii = pd.read_csv('./data/cleaned_data.csv')
#print(df_modii)