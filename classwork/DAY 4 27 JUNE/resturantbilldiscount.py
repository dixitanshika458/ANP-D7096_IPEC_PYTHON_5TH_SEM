# 6. Restaurant Bill Discount
# Problem Statement
# A restaurant offers discounts based on the total bill amount.
# • Bill below ₹1000 → No Discount
# • ₹1000–₹2999 → 10% Discount
# • ₹3000 or more → 20% Discount
# Write a Python program to determine the applicable discount.
# Sample Input
# 3200
# Sample Output
# 20% Discount Applied
bill_amount = float(input("Enter the total bill amount: "))
if bill_amount < 1000:
    print("No Discount")
elif bill_amount >= 1000 and bill_amount <= 2999:
    print("10% Discount Applied")
else:
    print("20% Discount Applied")
    #------------------------------------
    
