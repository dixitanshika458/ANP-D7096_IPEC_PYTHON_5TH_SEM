from numericcalculation import calculate_addition
print("----------------------------------------------------------------")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("----------------------------------------------------------------")
#calling addition function from numericcalculation module
print("Addition:", calculate_addition(num1, num2))
#calling subtraction function from numericcalculation module
print("Subtraction:", calculate_subtraction(num1, num2))
# ----------------------------------------------------------------
# Enter first number: 4
# Enter second number: 6
# ----------------------------------------------------------------
# Addition: 10
# Traceback (most recent call last):
#   File "c:\Users\priya dixit\Downloads\ANP-D7096_IPEC_PYTHON_5TH_SEM\batch 2\classwork\DAY 10 july 8\MODULE\example3.py", line 9, in <module>
#     print("Subtraction:", calculate_subtraction(num1, num2))
#                           ^^^^^^^^^^^^^^^^^^^^^
# NameError: name 'calculate_subtraction' is not defined. Did you mean: 'calculate_addition'?

