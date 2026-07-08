import numericcalculation as nc
print("----------------------------------------------------------------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#calling functions from numericcalculation module to perform calculations
print("----------------------------------------------------------------")
#calling addition function from numericcalculation module
print("Addition:", nc.calculate_addition(num1, num2))
#calling subtraction function from numericcalculation module
print("Subtraction:", nc.calculate_subtraction(num1, num2))
#calling multiplication function from numericcalculation module
print("Multiplication:", nc.calculate_multiplication(num1, num2))
#calling division function from numericcalculation module
print("Division:", nc.calculate_division(num1, num2))
#calling remainder function from numericcalculation module
print("Remainder:", nc.calculate_remainder(num1, num2)) 
print("----------------------------------------------------------------")