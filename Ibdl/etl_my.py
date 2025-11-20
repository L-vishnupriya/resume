import pandas as pd

# ------------------------ #
#        EXTRACT           #
# ------------------------ #
# Read data from CSV
df = pd.read_csv("input_data.csv")
print("Original Data:")
print(df)

# ------------------------ #
#      TRANSFORM           #
# ------------------------ #

# Rule 1: Remove rows where 'name' is null
df = df.dropna(subset=['name'])

# Rule 2: Standardize date format to YYYY-MM-DD
df['date_of_joining'] = pd.to_datetime(df['date_of_joining'], errors='coerce')

# Remove rows where date could not be parsed
df = df.dropna(subset=['date_of_joining'])

# Rule 3: Replace null salary with 0
df['salary'] = df['salary'].fillna(0)

print("\nCleaned & Transformed Data:")
print(df)

# ------------------------ #
#          LOAD            #
# ------------------------ #

# Load into a new CSV file
output_file = "C:\\Users\\vishn\\OneDrive\\Documents\\cleaned_output.csv"
df.to_csv(output_file, index=False)

print("\nData successfully loaded into:", output_file)
