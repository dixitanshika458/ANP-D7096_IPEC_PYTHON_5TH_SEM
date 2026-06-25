#find compound interest 
#taking input from user

c = float(input("enter the principal amount : "))
r = float(input("enter the rate of interest : "))
t = float(input("enter the time in years : "))

#----------------------------------------------------
#calculating compound interest
ci = c * (1 + r/100)**t - c
#----------------------------------------------------
#printing the compound interest

print("the compound interest is : ", ci)