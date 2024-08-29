#  Json is a syntax for storing/exchanging data.

import json

# Financial transaction record as a JSON-formatted string
x = """
{
  "date": "2024-08-28",
  "description": "Office Supplies Purchase",
  "category": "Office Expenses",
  "amount": -150.75,
  "transaction_type": "Debit",
  "account": "Business Checking",
  "vendor": "Stationery World",
  "payment_method": "Credit Card",
  "notes": "Purchased printer ink and paper"
}
"""

# 'loads()' Convert from JSON string to Python dictionary
y = json.loads(x)

print(y) # Output the Python dictionary

# 'dump()' Convert python obj to JSON str

# Economic data record -> GDP Report
gdp_record = {
    "year": 2024,
    "quarter": "Q2",
    "country": "United States",
    "gdp_value": 22000.5,  # in billion USD
    "growth_rate": 2.1,  # in percent
    "adjustment_type": "Seasonally Adjusted Annual Rate (SAAR)",
    "previous_quarter_gdp": 21850.3,  # in billion USD
    "sectors": {
        "agriculture": 450.2,  # in billion USD
        "industry": 5200.7,    # in billion USD
        "services": 16349.6    # in billion USD
    },
    "source": "Bureau of Economic Analysis (BEA)",
    "notes": "GDP growth driven by strong consumer spending and business investment."
}

gdp_json = json.dumps(gdp_record)

print(gdp_json)