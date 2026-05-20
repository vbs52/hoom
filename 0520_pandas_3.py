import pandas as pd


df = pd.read_csv("SuperMarket Analysis.csv")


df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

print("=== 資料筆數 ===")
print(len(df))

print("\n=== 前5筆資料 ===")
print(df.head())

filtered_df = df[
    (df['Branch'] == 'Alex') &
    (df['Customer type'] == 'Member')
]

print("\n=== Branch Alex 且 Member 資料 ===")
print(filtered_df.head())


product_summary = df.groupby('Product line').agg({
    'Sales': 'sum',
    'Rating': 'mean'
}).round(2)

print("\n=== Product line 分析 ===")
print(product_summary)

city_gender_summary = df.groupby(
    ['City', 'Gender']
).agg({
    'Sales': 'mean',
    'Invoice ID': 'count'
}).round(2)

city_gender_summary.rename(
    columns={
        'Sales': 'Average Sales',
        'Invoice ID': 'Transaction Count'
    },
    inplace=True
)

print("\n=== City + Gender 分析 ===")
print(city_gender_summary)

top_product_line = product_summary['Sales'].idxmax()

print("\n=== 總銷售額最高產品線 ===")
print(top_product_line)


product_summary.to_csv(
    "0520_pandas_3OK.csv"
)

print("\nCSV 檔案輸出完成！")