import pandas as pd

usa_sales_data = pd.read_csv("us_sales_2000_to_2016.csv")
products_data = pd.read_csv("product_master.csv")
merged_dataof_sales_products = pd.merge(products_data, usa_sales_data, on="ProductID")

merged_dataof_sales_products["Year"] = pd.to_datetime(merged_dataof_sales_products["Date"]).dt.year
# print(merged_dataof_sales_products)

result = merged_dataof_sales_products.groupby(["Year", "ProductID"])["Units"].sum()
# print(result.head(10))

top_product_ids = result.groupby('Year', group_keys=False).apply(lambda x: x.nlargest(5)).reset_index()
print(top_product_ids)



