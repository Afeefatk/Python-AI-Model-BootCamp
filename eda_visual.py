import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("land_prices.csv")
print(df.head())

# Visualize the distribution of land prices
sns.histplot(df["price_lakhs"], kde=True)
plt.xlabel("Price (Lakhs)")
plt.ylabel("Frequency")
plt.title("Distribution of Land Prices")
plt.show()

# Visualize the relationship between land area and price
sns.scatterplot(x="land_area_cents", y="price_lakhs", data=df)
plt.xlabel("Land Area (Cents)")
plt.ylabel("Price (Lakhs)")
plt.title("Land Area vs. Price")
plt.show()




df["price_per_cent"] = df["price_lakhs"] / df["land_area_cents"]
print(df[["land_area_cents", "price_lakhs", "price_per_cent"]].head())

## Distriubution analysis
sns.histplot(data=df, x="price_per_cent", kde=True)
plt.xlabel("Price per Cent (Lakhs)")
plt.ylabel("Frequency")
plt.title("Distribution of Price per Cent")
plt.show()

## Relation between 2 variables. detect outliers and trends
sns.scatterplot(data=df, x="size_in_sq_ft", y="price_per_cent")
plt.xlabel("Size in Sq Ft")
plt.ylabel("Price per Cent (Lakhs)")
plt.title("Land Size vs. Price per Cent")
plt.show()

## Comparing categories
sns.boxplot(data=df, x="taluk", y="price_per_cent")
plt.xlabel("Taluk")
plt.ylabel("Price per Cent (Lakhs)")
plt.title("Price per Cent by Taluk")
plt.show()