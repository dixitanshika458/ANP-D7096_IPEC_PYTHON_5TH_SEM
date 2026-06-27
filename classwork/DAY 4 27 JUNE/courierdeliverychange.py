# 3. Courier Delivery Charge
# Problem Statement
# A courier company calculates delivery charges based on the package weight.
# • Weight up to 2 kg → ₹50
# • Weight greater than 2 kg and up to 5 kg → ₹100
# • Weight greater than 5 kg → ₹180
# Write a Python program to display the delivery charge.
# Sample Input
# 4
# Sample Output
# Delivery Charge = ₹100
#--------------------------------------
weight = float(input("Enter the package weight in kg: "))
if weight <= 2:
    charge = 50
elif weight <= 5:
    charge = 100
else:
    charge = 180
print(f"Delivery Charge = ₹{charge}")
#--------------------------------------
#output
#package weight 