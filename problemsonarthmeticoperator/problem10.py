# 10. Event Management Budget
# Scenario:
# An event manager wants to calculate the cost contribution per participant.
# Problem Statement:
# Write a Python program to calculate how much each participant should pay.
# Input:
# • Total Event Cost
# • Number of Participants
# Output:
# • Amount per Participant 
total_event_cost = float(input("Enter the Total Event Cost: "))
num_participants = int(input("Enter the Number of Participants: "))
amount_per_participant = total_event_cost / num_participants
print("Each participant should pay:", amount_per_participant)
# Enter the Total Event Cost: 5000
# Enter the Number of Participants: 25
# Each participant should pay: 200.0
