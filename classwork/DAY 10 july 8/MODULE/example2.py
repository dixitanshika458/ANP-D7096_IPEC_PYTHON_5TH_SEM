#from numericalcalculation import 
from numericcalculation import * 
print("----------------------------------------------------------------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#calling functions from numericcalculation module to perform calculations
print("sum of ",num1,"and",num2,"is",calculate_addition(num1,num2))
#calling subtraction function from numericcalculation module
print("difference of ",num1,"and",num2,"is",calculate_subtraction(num1,num2))
#calling multiplication function from numericcalculation module
print("product of ",num1,"and",num2,"is",calculate_multiplication(num1,num2))
#calling division function from numericcalculation module
print("division of ",num1,"and",num2,"is",calculate_division(num1,num2))
#calling remainder function from numericcalculation module
print("remainder of ",num1,"and",num2,"is",calculate_remainder(num1,num2))
print("----------------------------------------------------------------")

