import pandas as pd

us_sales_data = pd.read_csv('us_sales_2000_to_2016.csv')

us_sales_data["Date"] =pd.to_datetime(us_sales_data['Date'])
us_sales_data["Year"] = us_sales_data['Date'].dt.year

us_sales_data["Quat"] = us_sales_data['Date'].dt.quarter

grouped_dataset  =us_sales_data.groupby(["Year","Quat"])["Units"].sum().reset_index()

print(grouped_dataset)
print(us_sales_data)

