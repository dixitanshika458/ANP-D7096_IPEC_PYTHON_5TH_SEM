# Problem 2: Parking Fee Waiver
# Problem Statement
# A shopping mall waives the parking fee if a customer has made purchases worth ₹2,000 or more.
# Otherwise, the customer must pay a parking fee of ₹100.
# Write a Python program to accept the purchase amount and display whether the parking fee is
# waived or payable.
#-------------------------------------
# Sample Input 1
# Enter the purchase amount: 2500
# Sample Output 1
# Parking Fee Waived!
# Parking Fee: ₹0
#--------------------------------------------------------------
# Sample Input 2
# Enter the purchase amount: 1500
# Sample Output 2
# Parking Fee Applicable!
# Parking Fee: ₹100
#--------------------------------------------------------------
#purchase amount input from user
purchase_amount = float(input("Enter the purchase amount: "))
#parking fee waiver condition
if purchase_amount >= 2000:
    print("Parking Fee Waived!")
    print("Parking Fee: ₹0")
    #else condition for purchase amount less than 2000
else:
    print("Parking Fee Applicable!")
    print("Parking Fee: ₹100")
    print("--------------------------------------------------------------")
#---------------------------------------------------------
#output:
#Enter the purchase amount: 5000
#Parking Fee Waived!
# Parking Fee: ₹0
#----------------------------------------------------------