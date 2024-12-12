import pandas as pd

# Load the CSV file
file_path = 'filtered_subjects.csv'  # Update with your CSV file path
df = pd.read_csv(file_path)

# Define category mapping
category_mapping = {
    'Fuze': 'Fuze/8x8'
}

# Print all unique categories from the 'Product - Service Desk Tool' column before aggregation
print("Original categories from CSV:")
print(df['Product - Service Desk Tool'].unique())

# Replace values in 'Product - Service Desk Tool' column based on the mapping
df['Product - Service Desk Tool'] = df['Product - Service Desk Tool'].replace(category_mapping)

# Group by 'Product - Service Desk Tool' and count total occurrences
aggregated_df = df.groupby('Product - Service Desk Tool').size().reset_index(name='Total Occurrences')

# Save the result to a new CSV file
output_file = 'aggregated_data.csv'
aggregated_df.to_csv(output_file, index=False)

print(f"Aggregated data has been saved to {output_file}")
