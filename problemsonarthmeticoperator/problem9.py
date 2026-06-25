# Problem Statement:
# Write a Python program to calculate the total recharge amount based on the data pack selected.
# Input:
# • Cost per GB
# • Number of GBs
# Output:
# • Total Recharge Cost

cost_per_gb = float(input("Enter the Cost per GB: "))
num_gbs = int(input("Enter the Number of GBs: "))
total_cost = cost_per_gb * num_gbs
print("The Total Recharge Cost is:", total_cost)
