import pandas as pd

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

df['Unit_Price'] = df['Unit_Price'].astype(str).str.replace('$', '', regex=False)
df['Unit_Price'] = df['Unit_Price'].str.replace(',', '', regex=False)

df['Stock_Quantity'] = df['Stock_Quantity'].astype(str).str.replace(',', '', regex=False)

df['Sales_Volume'] = df['Sales_Volume'].astype(str).str.replace(',', '', regex=False)

df['Unit_Price'] = pd.to_numeric(df['Unit_Price'], errors='coerce')
df['Stock_Quantity'] = pd.to_numeric(df['Stock_Quantity'], errors='coerce')
df['Sales_Volume'] = pd.to_numeric(df['Sales_Volume'], errors='coerce')

df['Total_Inventory_Value'] = (
    df['Stock_Quantity'] * df['Unit_Price']
)

print("=== 各商品總庫存價值 ===")
print(df[['Product_Name', 'Total_Inventory_Value']])

best_selling = df.loc[df['Sales_Volume'].idxmax()]

print("\n=== 最暢銷商品 ===")
print(best_selling['Product_Name'])

df['Discounted_Revenue'] = (
    df['Unit_Price'] * 0.9 * df['Sales_Volume']
)

print("\n=== 9折後收入 ===")
print(df[['Product_Name', 'Discounted_Revenue']])

total_revenue = df['Discounted_Revenue'].sum()

print("\n=== 9折後總收入 ===")
print(total_revenue)