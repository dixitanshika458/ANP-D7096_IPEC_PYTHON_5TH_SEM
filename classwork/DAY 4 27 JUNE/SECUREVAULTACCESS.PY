# 1. Secure Vault Access
# Problem Statement
# A digital vault can only be opened if the user enters the correct security code.
# Write a Python program that accepts the entered security code. If the entered code is 7890, display:
# "Access Granted to the Vault."
# Otherwise, do nothing.
# Sample Input
# 7890
# Sample Output
# Access Granted to the Vault.
#--------------------------------------
security_code = int (input("Enter the four digit security code: "))
#validating security code input
if security_code < 1000 or security_code > 9999:
    exit("Invalid security code." )
#verifying whether the entered security code is correct
if security_code == 7890:
    print("Access Granted to the Vault.")
else:
    print("Invalid security code.")
#---------------------------------------
'''output
Enter the four digit security code: 7890
Access Granted to the Vault.
-----------------------------------------'''