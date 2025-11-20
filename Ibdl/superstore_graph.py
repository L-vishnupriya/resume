import pandas as pd
import matplotlib.pyplot as plt

# -------------------- #
#     STEP 1: LOAD     #
# -------------------- #
df = pd.read_csv("Superstore.csv", encoding='latin1')
print("Original Data Loaded")
print(df.head())

# -------------------- #
#   STEP 2: CLEANING   #
# -------------------- #

# Convert date field
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Drop rows with important missing values
df = df.dropna(subset=['Sales', 'Profit', 'Category', 'Region'])

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df.head())

# --------------------------- #
#   STEP 3: ANALYSIS INSIGHTS #
# --------------------------- #

# Insight 1: Sales by Category
sales_by_category = df.groupby('Category')['Sales'].sum()

# Insight 2: Profit by Region
profit_by_region = df.groupby('Region')['Profit'].sum()

print("\nSales by Category:")
print(sales_by_category)

print("\nProfit by Region:")
print(profit_by_region)

# --------------------------- #
#     STEP 4: VISUALIZATION   #
# --------------------------- #

# Plot 1: Sales by Category
plt.figure(figsize=(8,5))
sales_by_category.plot(kind='bar')
plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Plot 2: Profit by Region
plt.figure(figsize=(8,5))
profit_by_region.plot(kind='bar')
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()
