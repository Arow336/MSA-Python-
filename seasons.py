#Function: To get the name of the season
#Input: (int)season_no
#Output: (string)name of the month
def get_season_name(season_no:int):

    if season_no in [12,1,2]:
        return "Winter"
    elif season_no in [3,4,5]:
        return "Spring"
    elif season_no in [6,7,8]:
        return "Summer"
    elif season_no in [9, 10,11]:
        return "Fall"
    else: 
        return "Invalid Number"


#Function: 
#Input: 
#Output: (int)number of the mont
def get_month_number():
    #validate the input is 1 -12
    #reprompt user if input not valid 
    while True: 
        try: 
            season_no = int(input("Enter a month number: "))
            if season_no < 1:
                print ("Please enter a value greater than 0: ")
                continue
            elif season_no > 12: 
                print ("Please enter a valid month number (less than 12): ")
            else: 
                break 
        except:
            print("Please enter a valid number: ")
    
    return season_no

    


def main():
    condition = True
    while condition: 
        #Call the prompt get_month_number function to prompt and get the month number from the user
        month_no = get_month_number()
        #Call the get_season_name function to get the name of the season
        season_name = get_season_name(month_no)
        #print the output
        print (f"The Season is {season_name}")
        #ask the user if they want to run the program again
        prompt = input ("Enter y to continue (enter any other letter to quit): ")

        #if y or Y rerun the program, otherwise end the program
        if ((prompt == "Y") or (prompt == "y")):
            condition = True
        else: 
            condition = False


main()