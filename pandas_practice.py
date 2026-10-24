import pandas as pd

# Create a simple DataFrame
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [1000, 50, 80, 300]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)


df_student = pd.read_csv("students_data.csv")
print("Student DataFrame:\n", df_student)

print("Student DataFrame Info:\n", df_student.info())
print("Student DataFrame Description:\n", df_student.describe())

print(df_student["grade"].describe())