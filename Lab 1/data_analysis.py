import pandas as pd
# Load sample CSV data
df = pd.read_csv(r'C:\Users\kiner\OneDrive\Desktop\cps3320\Lab 1\sample.csv')
# Display basic information
print(df.info())
# Display the first 5 rows of the dataframe
print(df.head())