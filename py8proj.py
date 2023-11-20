import pandas as pd


us_sales_data = pd.read_csv("us_sales_2000_to_2016.csv")
products_data_set = pd.read_csv("product_master.csv")

new = pd.merge(products_data_set, us_sales_data, on="ProductID")
new["year"] = pd.to_datetime(new["Date"]).dt.year
# print(new)

recent_two_years = new[new["year"].isin([2015, 2016])]
# print(recent_two_years)

result = recent_two_years.groupby(["year", "ProductID"])["Units"].sum().unstack()
# print(result)

diff_in_units = result.diff(axis=0).fillna(0)
# print(change_in_units)

final_change = diff_in_units.abs().sum(axis=0)
# print(total_change)

top_product = final_change.nlargest(1).index

print(products_data_set.loc[top_product]['Product'].reset_index())
