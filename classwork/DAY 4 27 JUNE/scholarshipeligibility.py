# 2. Scholarship Eligibility
# Problem Statement
# A university provides a scholarship only to students who score 90 or above.
# Write a Python program to accept a student's percentage and determine whether the student is eligible.
# • If percentage is 90 or above, display:
# Scholarship Approved
# • Otherwise display:
# Scholarship Not Approved
# Sample Input
# 92
# Sample Output
# Scholarship Approved
#--------------------------------------
percentage = float(input("Enter the student's percentage: "))
#validating percentage input
if percentage < 0 or percentage > 100:
    exit("Invalid percentage." )
#verifying whether the student is eligible for scholarship
if percentage >= 90:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")
#---------------------------------------
'''output
student percentage = 97
scholarship approved
-----------------------------------------'''