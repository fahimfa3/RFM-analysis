import sqlite3
import pandas as pd

# Load clean data
df = pd.read_csv('/Users/sumerafaisal/BI_proj_1/data/retail_cleaned.csv')

# Create database connection
conn = sqlite3.connect('retail.db')

# Load to SQL
df.to_sql('customers', conn, if_exists='replace', index=False)

conn.close()

print("Data successfully loaded to database!")