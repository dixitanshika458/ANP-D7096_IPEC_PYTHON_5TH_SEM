# Problem 3: Loan Eligibility Check
# Problem Statement
# A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or
# more.
# Write a Python program to accept the applicant's monthly salary and display whether they are
# eligible to apply for the loan.
# Sample Input 1
# Enter your monthly salary: 45000
# Sample Output 1
# Congratulations! You are eligible to apply for the loan.
# Sample Input 2
# Enter your monthly salary: 22000
# Sample Output 2
# Sorry! You are not eligible to apply for the loan..
#--------------------------------------------------------------
#monthly salary input from user
monthly_salary = float(input("Enter your monthly salary: "))
#loan eligibility condition
if monthly_salary >= 30000:
    print("Congratulations! You are eligible to apply for the loan.")
    #else condition for monthly salary less than 30000  
else:
    print("Sorry! You are not eligible to apply for the loan.")
    print("--------------------------------------------------------------")
    #---------------------------------------------------------
    #output:
    #Enter your monthly salary: 35000
#Congratulations! You are eligible to apply for the loan.
#--------------------------------------------------------------
