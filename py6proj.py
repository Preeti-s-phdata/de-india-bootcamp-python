import pandas as pd

usa_sales_data_extract = pd.read_csv("us_sales_2000_to_2016.csv")
products_sales_data = pd.read_csv("product_master.csv")
usa_master_sales_data = pd.read_csv("zip_usa_master.csv")

us_master_data_copy = usa_master_sales_data.copy(deep=True)
us_master_data_copy.rename(columns={"PostalCode" : "Zip"}, inplace=True)
# print(us_master_data_copy)
new_famous = pd.merge(us_master_data_copy, usa_sales_data_extract, on="Zip")
# print(new_famous)
result = new_famous[new_famous["PlaceName"] == "Fort Worth"]

x = result.groupby("ProductID")["Units"].sum().idxmax()
print("Famous product in Fort Worth, Texas :", products_sales_data[products_sales_data["ProductID"] == x]["Product"].values)