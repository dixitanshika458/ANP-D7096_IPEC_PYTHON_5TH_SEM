# 3. Fuel Consumption Tracker
# Scenario:
# A person wants to calculate the average fuel consumption of a car.
# Problem Statement:
# Write a Python program to find the average mileage of a car.
# Input:
# • Total distance traveled (km)
# • Fuel consumed (liters) 
# Fuel Consumption Tracker
distance = float(input("Enter the total distance traveled (in km): "))
fuel = float(input("Enter the fuel consumed (in liters): "))
average_mileage = distance / fuel
print("The average mileage of the car is:", average_mileage, "km/l")
