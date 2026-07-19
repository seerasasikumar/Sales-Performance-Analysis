import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Superstore_Sales.csv")
print(df.head())
df.info()
print(df.isnull().sum())
df.dropna(inplace = True)
print(df.duplicated().sum())
df.drop_duplicates(inplace = True)

print("Total Sales =",df["Sales"].sum())
print("Total Profit =",df["Profit"].sum())
print("Total Orders =",df["Order_ID"].count())
print("Average Order Value =",df["Sales"].mean())

Category_Sales = df.groupby("Category")["Sales"].sum()
Category_Sales = Category_Sales.sort_values(ascending = False)
print(Category_Sales)

Top_Products = df.groupby("Product_Name")["Sales"].sum()
Top_Products = Top_Products.sort_values(ascending = False).head(8)
print(Top_Products)

Top_Customers = df.groupby("Customer_Name")["Sales"].sum()
Top_Customers = Top_Customers.sort_values(ascending = False).head()
print(Top_Customers)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month
Monthly_Sales = df.groupby("Month")["Sales"].sum()
print(Monthly_Sales)

Profit_by_Category = df.groupby("Category")["Profit"].sum()
print(Profit_by_Category)

Profit_Margin = (df["Profit"].sum() / df["Sales"].sum()) * 100
print(Profit_Margin)

Region_Sales = df.groupby("Region")["Sales"].sum()
Region_Sales = Region_Sales.sort_values(ascending = False)
print(Region_Sales)


Category_Sales.plot(kind = "bar")
plt.title("Sales by category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

Monthly_Sales.plot(kind = "line")
plt.title("Month Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

Top_Products.plot(kind = "bar")
plt.title("Top Products")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.show()

Top_Customers.plot(kind = "bar")
plt.title("Top Customers")
plt.xlabel("Customer")
plt.ylabel("Amount")
plt.show()

Profit_by_Category.plot(kind = "bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

Region_Sales.plot(kind = "bar")
plt.title("Region Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
