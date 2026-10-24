import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# Show every column without truncation
pd.set_option('display.max_columns', None)

df = pd.read_csv("land_prices.csv")
print(df.info())
print(df.head())


df["price_per_cent"] = df["price_lakhs"] / df["land_area_cents"]
print(df.head())


## Covert categorical data into numerical values using one-hot encoding

print(df.columns)

numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()



# ##Convert property_id to integer type
# df["property_id"] = df["property_id"].astype(int)

categorical_features = df.select_dtypes(include=[object]).columns.tolist()
print("Categorical features:", categorical_features)

df_processed = pd.get_dummies(df, columns=categorical_features, drop_first=True)
print(df_processed.head())

dummy_features = [col for col in df_processed.columns if col not in numeric_features]
print("Dummy features:", dummy_features)

# Dropping some unnecessary numeric features if needed
numeric_features = [col for col in numeric_features if col not in ["property_id", "latitude", "longitude", "price_lakhs", "price_per_cent"]]
print("Numeric features:", numeric_features)

## Just get the new dummy features after one-hot encoding

features = numeric_features + dummy_features
print("Features:", features)





X = df_processed[features]
y = df_processed["price_per_cent"]
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# Choose model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

## Evaluation
y_pred = model.predict(X_test)

print("Mean Absolute Error:", metrics.mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("R^2 Score:", metrics.r2_score(y_test, y_pred))



prediction_df = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})
print(prediction_df.head()) 


## Try new predictions with different input data
features_list = model.feature_names_in_.tolist()
print(features_list)

new_data = pd.DataFrame(columns=features_list)
print(new_data.head())


# number of columns in the new data
print("Number of columns in new data:", new_data.shape[1])

# Example: Fill in new data for prediction
new_data.loc[0] = [6, 1, 18, 7, 1, 3, 0.5, 1.5,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]  # Replace with actual values for all features
prediction = model.predict(new_data)
print("Prediction for new data:", prediction)