# . Compound Growth of Savings
# Scenario:
# A person invests money and wants to see how the amount grows over years.
# Problem Statement:
# Write a Python program to calculate the value of money after a certain number of years assuming it
# doubles every year.
# Input:
# • Initial Amount
# • Number of Years
# Output:
# • Final Amount
# 8. Online Shopping Disc
initial_amount = float(input("Enter the Initial Amount: "))
years = int(input("Enter the Number of Years: "))

final_amount = initial_amount * (2 ** years)
print("The Final Amount after", years, "years is:", final_amount)
# Enter the Initial Amount: 1000
# Enter the Number of Years: 5
# The Final Amount after 5 years is: 32000.0
