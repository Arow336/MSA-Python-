# Write a program that calculates the wages of a worker
# A user will be prompted for the amounts of hours they worked
# and thei wages per hour
# the program will calculate the total wages of the worker after a 12% deduction 
# per year. 
# the program will print a pay advice containing the following information: hours worked
# hourly wage, wages before taxes, tax amount, and annual wages after taxes

#GET INPUT FROM THE USER 
# Get the hourly wage and the amount of hours worked from the user
# convert both the hourly wage and the amount of hours to a float
# Validate that the hours worked is less than 24 but greater than 0 


def get_accurate_amount_of_hours_worked():
    while True: 
        try: 
            hours_worked= float(input("Enter the amount of hours worked: ")) 
            # validate that user hours is greater than 0
            if hours_worked <= 0:
                print("ERROR: Enter a value greater than 0")
                continue
            # validate that user hours worked is less than or equal to 24
            elif hours_worked > 24: 
                print("ERROR: Enter a value withing the hours of A day: ")
                continue
            else: 
                break 
        except: 
            print ("ERROR: Please enter a valid number: ")
    
    return hours_worked 

def get_accurate_hourly_wage(): 
    while True:
        try:
            wages_per_hour = float(input("Enter your hourly wage: "))
            #validate that hourly wage is greater than 0
            if wages_per_hour <= 0:
                print ("ERROR: Enter a value greater than 0")
                continue
            else: 
                break
        except: 
            print ("ERROR: Please enter a valid number: ")
    
    return wages_per_hour 



def main(): 
    #get hours worked from the user. Call the get_accurate_amount_of_hours_worked function
    hours_worked = get_accurate_amount_of_hours_worked() 
    # get hourly wage from the user
    hourly_wage = get_accurate_hourly_wage()

    #calculate the daily wage of the user 
    daily_wage = hours_worked * hourly_wage 

    #calculate the yearly wage of the user without taxes 
    yearly_wage_without_taxes = daily_wage * 350 

    #calculate the annual tax amount 
    tax_amount = 0.12 * yearly_wage_without_taxes 

    #calculate the annual wage of the user with tax deductions 
    yearly_wage_with_taxes = yearly_wage_without_taxes - tax_amount 

    # Printing out the pay advice for the user 
    print ("\nPay Advice ")
    print ("------------")
    print(f"Hours Worked: {hours_worked}")
    print (f"Hourly Wage: ${hourly_wage}")
    print (f"Wages Before Taxes: ${yearly_wage_without_taxes:.2f}")
    print (f"Tax Amount: ${tax_amount:.2f}")
    print (f"Annual Wage after taxes: ${yearly_wage_with_taxes:.2f}")


main()