import pandas as pd

# Create a dictionary from a DataFrame
# new_dict = {new_key: new_value for (index,value) in df.iterrows() if condition}

# Sample data for data security incidents
data_security_records = [
    {"Date": "2024-01-01", "Incident Type": "Data Breach", "Description": "Unauthorized access to sensitive customer data", "Affected Entity": "ABC Corp", "Impact": "High"},
    {"Date": "2024-01-05", "Incident Type": "Phishing Attack", "Description": "Phishing emails targeting employees", "Affected Entity": "XYZ Inc", "Impact": "Medium"},
    {"Date": "2024-01-10", "Incident Type": "Ransomware", "Description": "Ransomware attack encrypting company files", "Affected Entity": "123 Ltd", "Impact": "Critical"},
    {"Date": "2024-01-12", "Incident Type": "Data Leak", "Description": "Accidental exposure of sensitive data", "Affected Entity": "DEF LLC", "Impact": "Low"},
    {"Date": "2024-01-15", "Incident Type": "Insider Threat", "Description": "Malicious actions by a disgruntled employee", "Affected Entity": "GHI Corp", "Impact": "High"},
    {"Date": "2024-01-20", "Incident Type": "DDoS Attack", "Description": "Distributed denial-of-service attack on website", "Affected Entity": "JKL Inc", "Impact": "Medium"},
    {"Date": "2024-01-22", "Incident Type": "Data Breach", "Description": "Compromise of user accounts", "Affected Entity": "MNO Ltd", "Impact": "High"},
    {"Date": "2024-01-25", "Incident Type": "Malware Infection", "Description": "Malware detected on corporate network", "Affected Entity": "PQR LLC", "Impact": "Critical"},
    {"Date": "2024-01-28", "Incident Type": "Social Engineering", "Description": "Social engineering attack on executives", "Affected Entity": "STU Corp", "Impact": "Medium"},
    {"Date": "2024-01-30", "Incident Type": "Data Leak", "Description": "Sensitive information exposed via unsecured database", "Affected Entity": "VWX Inc", "Impact": "High"},
    {"Date": "2024-02-02", "Incident Type": "Phishing Attack", "Description": "Spear phishing targeting financial department", "Affected Entity": "YZA Ltd", "Impact": "Critical"},
]

# Creating the DataFrame
df = pd.DataFrame(data_security_records)

# Iterating over DataFrame rows with df.iterrows() to access each row's index and data (as a Series) for row-wise operations.
for (index, row) in df.iterrows():
    print(row['Incident Type']) # Access and print the value of the 'Incident Type' column for each row

