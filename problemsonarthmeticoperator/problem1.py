# 1. Monthly Salary Calculation
# Scenario:
# A company pays an employee a fixed monthly salary and additional incentives based on performance.
# Problem Statement:
# Write a Python program to calculate the total monthly salary of an employee by adding the fixed salary
# and incentive amount.
# Input:
# • Basic Salary
# • Incentive
# Output:
# • Total Salary
# salary = float(input("Enter the basic salary : "))
# incentive = float(input("enter the incentive amount :"))
# print("the basic salary" , salary)
# print("the incentive amount", incentive)
# print("the final amount" , salary+incentive)
#Enter the basic salary : 130000
#enter the incentive amount : 5000
#the basic salary 130000.0
#the incentive amount 5000.0
#the final amount 135000.0
#2. Grocery Store Bill
#Scenario:
#A customer purchases multiple packets of rice from a grocery store.
#Problem Statement:
# Write a Python program to calculate the total cost of rice packets purchased.
# Input:
# • Price per packet
# • Number of packets
# Output:
# • Total Bill Amount 

price_per_packet = float(input("Enter the price per packet: "))
num_packets = int(input("Enter the number of packets: "))
total_bill = price_per_packet * num_packets
print("The Total Bill Amount is:", total_bill)
