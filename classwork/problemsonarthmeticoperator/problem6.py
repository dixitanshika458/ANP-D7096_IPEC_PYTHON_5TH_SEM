# 6. Pizza Distribution
# Scenario:
# A party organizer wants to distribute pizza slices equally among children.
# Problem Statement:
# Write a Python program to find how many slices remain after equal distribution.
# Input:
# • Total Pizza Slices
# • Number of Children
# Output:
# • Remaining Slices
# Pizza Distribution Program

total_slices = int(input("Enter the total number of pizza slices: "))
num_children = int(input("Enter the number of children: "))

remaining_slices = total_slices % num_children
print("The number of remaining slices is:", remaining_slices)
# Enter the total number of pizza slices: 17
# Enter the number of children: 5
# The number of remaining slices is: 2
