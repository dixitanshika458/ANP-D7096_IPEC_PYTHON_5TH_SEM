# Problem 1: Electricity Bill Discount
# Problem Statement
# An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000
# or more. Otherwise, no discount is applied.
# Write a Python program to accept the total bill amount from the user and display the final amount to
# be paid.
# Sample Input 1
# Enter the electricity bill amount: 6200
# Sample Output 1
# Discount Applied!
# Final Bill Amount: ₹5580.0
# Sample Input 2
# Enter the electricity bill amount: 4200
# Sample Output 2
# No Discount Applied!
# Final Bill Amount: ₹4200
electricity_bill = float(input("Enter the electricity bill amount: "))
if electricity_bill >= 5000:
    discount = electricity_bill * 0.10
    final_amount = electricity_bill - discount
    print("Discount Applied!")
    print(f"Final Bill Amount: ₹{final_amount}") 
else:
    print("No Discount Applied!")
    print(f"Final Bill Amount: ₹{electricity_bill}")
   