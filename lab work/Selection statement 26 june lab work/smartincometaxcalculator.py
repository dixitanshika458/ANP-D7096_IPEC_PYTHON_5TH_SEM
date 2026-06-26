# . Smart Income Tax Calculator 
# Problem Statement 
# A government tax portal calculates tax based on the following conditions: 
# • Income up to ₹5,00,000 → No tax  
# • ₹5,00,001 to ₹10,00,000 → 10%  
# • ₹10,00,001 to ₹20,00,000 → 20%  
# • Above ₹20,00,000 → 30%  
# Additional Benefits: 
# • Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
# • Women taxpayers receive an additional 2% rebate on tax.  
# Write a Python program to calculate the final tax amount payable. 
# Sample Input 
# Enter Annual Income: 1200000 
# Enter Age: 65 
# Enter Gender (M/F): F 
# Sample Output 
# Tax before rebate: ₹240000.0 
# Senior Citizen Rebate: ₹12000.0 
# Women Rebate: ₹4800.0 
# Final Tax Payable: ₹223200.0
income = float(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ")
if income <= 500000:
    tax = 0
elif income <= 1000000:
    tax = (income - 500000) * 0.10  
elif income <= 2000000:
    tax = (income - 1000000) * 0.20 + 50000
else:
    tax = (income - 2000000) * 0.30 + 250000
senior_citizen_rebate = 0
if age >= 60:
    senior_citizen_rebate = tax * 0.05
    print(f"Senior Citizen Rebate: ₹{senior_citizen_rebate}")
    if gender.upper() == 'F':
        women_rebate = tax * 0.02
        print(f"Women Rebate: ₹{women_rebate}")
        final_tax = tax - senior_citizen_rebate
        final_tax = final_tax - women_rebate
    else:
        final_tax = tax - senior_citizen_rebate 
        print(f"Final Tax Payable: ₹{final_tax}")
        #-------------------------------------------
        #output
#         Enter Annual Income: 1200000
# Enter Age: 65
# Enter Gender (M/F): F
# Tax before rebate: ₹240000.0
# Senior Citizen Rebate: ₹12000.0
# Women Rebate: ₹4800.0
# Final Tax Payable: ₹223200.0
#----------------------------------------------------



              
              

    
