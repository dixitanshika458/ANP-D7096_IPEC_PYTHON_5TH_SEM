# 7. Exam Hall Entry 
# Problem Statement 
# Students are allowed to enter the examination hall only if they are carrying their admit card. 
# Accept input as: 
# • 1 → Admit Card Available  
# • 0 → Admit Card Not Available  
# If the input is 1, display: 
# Enter Examination Hall 
# Otherwise, do not display anything. 
# Sample Input 
# 1 
# Sample Output 
# Enter Examination Hall
#------------------------------------
admit_card = int(input("Enter 1 if Admit Card is Available, 0 if Not Available: "))
if admit_card == 1:
    print("Enter Examination Hall")
else:
    print("Admit Card Not Available. Entry Denied.")
    #------------------------------------
    #output:
    
