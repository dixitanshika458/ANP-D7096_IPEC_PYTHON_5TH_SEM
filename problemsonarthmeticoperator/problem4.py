# 4. Bank Account Balance
# Scenario:
# A customer withdraws money from their bank account.
# Problem Statement:
# Write a Python program to calculate the remaining balance after withdrawal.
# Input:
# • Current Balance
# • Withdrawal Amount
# Output:
# • Remaining Balance 
# Bank Account Balance Program

current_balance = float(input("Enter your current balance: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))

remaining_balance = current_balance - withdrawal_amount
print("The Remaining Balance is:", remaining_balance)
