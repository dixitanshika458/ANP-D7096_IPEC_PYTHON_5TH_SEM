from twodfigures import *
x = """ select the shape with the number
o select 1 for square
o select 2 for circle   
o select 3 for triangle
o select 4 for rectangle"""
print(x)
shape = int(input("Enter the number of the shape you want to calculate: "))
#---------------------------------------------------------------------------
if shape == 1:
    op = """Enter 1 for area and 2 for perimeter"""
    operation = int(input("enter the operation you want to perform: "))
    side = float(input("Enter the side in m "))
    if side <= 0:
        exit("Error: Side length must be a positive number.")
    if operation == 1:
        print("The area of the square is: ", square_area(side), "m^2")
    elif operation == 2:
        print("The perimeter of the square is: ", square_perimeter(side), "m")
#------------------------------------------------------------------------------    
if shape == 2:
    op = """Enter 1 for area and 2 for perimeter"""
    operation = int(input("enter the operation you want to perform: "))
    radius = float(input("Enter the radius in m "))
    if radius <= 0:
        exit("Error: Radius must be a positive number.")
    if operation == 1:
        print("The area of the circle is: ", circle_area(radius), "m^2")
    elif operation == 2:
        print("The perimeter of the circle is: ", circle_circumference(radius), "m")
#-----------------------------------------------------------------------------------
if shape == 3:
    op = """Enter 1 for area and 2 for perimeter"""
    operation = int(input("enter the operation you want to perform: "))
    base = float(input("Enter the base in m "))
    height = float(input("Enter the height in m "))
    if base <= 0 or height <= 0:
        exit("Error: Base and height must be positive numbers.")
    if operation == 1:
        print("The area of the triangle is: ", triangle_area(base, height), "m^2")
    elif operation == 2:
        print("The perimeter of the triangle is: ", triangle_perimeter(base, height), "m")
#-----------------------------------------------------------------------------------
if shape == 4:
    op = """Enter 1 for area and 2 for perimeter"""
    operation = int(input("enter the operation you want to perform: "))
    length = float(input("Enter the length in m "))
    width = float(input("Enter the width in m "))
    if length <= 0 or width <= 0:
        exit("Error: Length and width must be positive numbers.")
    if operation == 1:
        print("The area of the rectangle is: ", rectangle_area(length, width), "m^2")
    elif operation == 2:
        print("The perimeter of the rectangle is: ", rectangle_perimeter(length, width), "m")
#-----------------------------------------------------------------------------------------





        
