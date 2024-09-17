import pandas as pd

FILE_PATH = './data/raw_data.csv'

df = pd.read_csv(FILE_PATH)

ru_list = df.values.tolist()

print(ru_list)