'''
monthly installment
'''
loan_value = int(input("Please enter the loan value: "))
years = int(input("Please enter the number of years: "))
ans = (loan_value+0.12*loan_value*years)/(12*years)
print(f"Your monthly installment is {ans} EGP")