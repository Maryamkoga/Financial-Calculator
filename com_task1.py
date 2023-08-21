# program that will allow user access two different financial calculators
# The user will enter a choice of either calculator
import math
print("investment - to calculate the amount of interest you'll earn on your investment ")
print("bond - to calculate the amount of interest you'll have to pay on a home loan")

option_1 = "investment"
option_2 = "bond"

#While loop for user input error
while True:
    try:
        user_input = input("Enter either 'investment' or 'bond' to proceed: ")
        if user_input.lower() != option_1 and user_input != option_2:
            raise ValueError("Invalid input. Please try again.")
        break
    except ValueError as error:
        print(error)

#user input will take in all selections
#user picks either investment and enters the necessary details
if user_input.lower() == option_1:
    while True:  
        try:
            p = float(input("Enter the amount of money you will be depositing: "))
            r = float(input("Enter interest rate without percentage:"))
            t = int(input("Enter number of years to invest:"))
            if p < 0 or r < 0 or t < 0:
                raise ValueError("Please enter non-negative values.")
            break
        except ValueError as error:
            print(error)

    #Creating a variable to change rate from percentage
    real_r = r * 0.01

    #Get user input for the type of interest to calculate
    while True:
        try:
            interest = input("Enter either 'simple' or 'compound' interest: ")
            if interest != "simple" and interest != "compound":
                raise ValueError("Invalid input. Please try again.")
            break
        except ValueError as error:
            print(error)

    #Calculate either simple or compound interest
    if interest == "simple":
        A = p *(1 + real_r*t)    
        print("The Simple Interest is " , A) 
    elif interest == "compound":
        A2 = p * math.pow((1 + real_r), t)
        print("The Compound Interest is " , A2)
        
#User picks bond calculator
elif user_input .lower() == option_2 .lower():
    while True:
        try:
            p = float(input("Enter the present value of the house: "))
            i = float(input("Enter interest rate without percentage: "))
            n = int(input("Enter number of months to repay bond: "))
            if p < 0 or i < 0 or n < 0:
                raise ValueError("Please enter non-negatuve values.")
            break
        except ValueError as error:
            print(error)

#created a variable to change interest from percentage
    real_i = i * 0.01 / 12
    
#calculating bond repayment
    repayment = (real_i * p)/(1 - (1 + real_i)**(-n))
    print("Amount to be repayed each month is " , repayment)
