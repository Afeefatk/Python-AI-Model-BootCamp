import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv("study_habits.csv")
print(df.info())

## Define variables
X = df[["study_hours_without_mobile_usage"]]
Y = df["average_score_percentage"]

## Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

## Create Model, Train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

## Evaluate, Make predictions
Y_pred = model.predict(X_test)

## Evaluate the model
print("Mean Squared Error:", metrics.mean_squared_error(Y_test, Y_pred))
print("R2 Score:", metrics.r2_score(Y_test, Y_pred))


prediction_df = pd.DataFrame({"Actual": Y_test, "Predicted": Y_pred})
print(prediction_df)


n1_X = pd.DataFrame([[3]])
n1_pred = model.predict(n1_X)
print("Prediction for 3 study hours without mobile usage:", n1_pred)