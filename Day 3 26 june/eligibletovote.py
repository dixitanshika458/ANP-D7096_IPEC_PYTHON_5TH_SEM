#write a program to check whether a person is eligible to vote or not. A person is eligible to vote if his/her age is greater than or equal to 18.
#input of age from user
print("--------------------------------------------")
age = int(input("Enter your age: "))
#to validate age of the person
if(age <= 0):
    exit("Age must be positive")
#verifying eligibility of the person
if(age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("--------------------------------------------")
#-----------------------------------------------------
#output:
#Enter your age: 20
#You are eligible to vote.
#-----------------------------------------------------
