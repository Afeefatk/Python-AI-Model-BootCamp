import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr2)




product_prices = [100,200,500,1000]
prod_array = np.array(product_prices)
print("Product prices array:", prod_array)

product_discount_amount = prod_array * 0.05
print("Product discount amount array:", product_discount_amount)