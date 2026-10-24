import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("land_prices.csv")
print(df.head())

df_loaction_prices = df[["location_name", "price_lakhs"]]
print(df_loaction_prices.head())

df_size_prices = df[["land_area_cents", "price_lakhs"]]
print(df_size_prices.head())