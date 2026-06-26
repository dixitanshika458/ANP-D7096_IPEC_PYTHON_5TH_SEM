# Problem Statement 3 : Student Grade Calculator
# A school assigns grades based on the marks obtained by students according to the following criteria:
# * Marks 90 and above → Grade A
# * Marks 75 to 89 → Grade B
# * Marks 50 to 74 → Grade C
# * Below 50 → Grade F
#--------------------------------------------------------------
# Write a Python program to accept marks from the user and display the corresponding grade.
# Sample Input
# Enter Marks: 92
# Sample Output
# Grade A
#--------------------------------------------------------------
# Sample Input
# Enter Marks: 80
# Sample Output
# Grade B
#--------------------------------------------------------------
# Sample Input
# Enter Marks: 65
# Sample Output
# Grade C
#--------------------------------------------------------------
# Sample Input
# Enter Marks: 35
# Sample Output
# Grade F
#--------------------------------------------------------------
#marks input from user
marks = float(input("Enter Marks: "))
#grade assignment based on marks
if marks >= 90:
    print("Grade A")
    #marks between 75 and 89
elif marks >= 75:
    print("Grade B")
    #marks between 50 and 74
elif marks >= 50:
    #marks between 50 and 74
    print("Grade C")
    #marks below 50
else:
    print("Grade F")
#--------------------------------------------------------------
#output:
#Enter Marks: 92
#Grade A
#--------------------------------------------------------------