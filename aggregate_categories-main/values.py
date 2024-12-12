import pandas as pd

# Path to your CSV file
csv_file = "current_fields.csv"

# Load the CSV into a pandas DataFrame
df = pd.read_csv(csv_file)

# Extract the 'value' column
value_column = df[['value']]

# Save the extracted column to a new CSV (optional)
value_column.to_csv("value_column.csv", index=False)

# Print the extracted values (optional)
print(value_column)
