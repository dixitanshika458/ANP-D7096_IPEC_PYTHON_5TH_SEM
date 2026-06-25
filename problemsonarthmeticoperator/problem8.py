# 8. Online Shopping Discount
# Scenario:
# An e-commerce website offers a fixed discount on products.
# Problem Statement:
# Write a Python program to calculate the final payable amount after applying the discount.
# Input:
# • Product Price
# • Discount Amount
# Output:
# • Final Price
product_price = float(input("Enter the Product Price: "))
discount_amount = float(input("Enter the Discount Amount: "))
final_price = product_price - discount_amount
print("The Final Price after discount is:", final_price)
