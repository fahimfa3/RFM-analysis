import pandas as pd

df = pd.read_csv('/Users/sumerafaisal/Downloads/Online Retail 1(Online Retail).csv', encoding='ISO-8859-1')
# Remove rows with missing values
df = df.dropna(subset=['CustomerID'])
# Remove rows with negative or zero quantity
df = df[df['Quantity'] > 0]
# Remove rows with negative or zero price
df = df[df['UnitPrice'] > 0]
# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# Create a new column for total price
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
# Save the cleaned data to a new CSV file
df.to_csv('retail_cleaned.csv', index=False)