#This file demonstrates decision structures and conditions
def main():
    a = 6
    b = 17

    #Exploring conditions
    print(f"A is greater than B: {a > b}")
    print(f"B is greater than A: {b > a}")
    print(f"A is equal to B: {a == b}")

    #Comparison operators:
    # less than: <, greater than >, less than or equal to <=, greater than or equal to >=
    # equal to: ==

    #create a decision structure to determine if a and b are equal
    if a > b: 
        print (f"{a} is greater and {b}")
    elif b > a: 
        print(f"{b} is greater than {a}")
    else: 
        print(f"{a} is equal to {b}")
        
    #create a decision structure to print a letter grade based 
    # on a test score 
    # A : 100 - 90, B: 89 - 80, C: 79- 70, D: 69 - 60, F less than 60
    print("Grade Decision: 1")
    test_score = 110

    if((test_score <= 100) and (test_score >= 90)): 
        print(f"{test_score} -- > A")
    elif ((test_score >= 80)):
        print (f"{test_score} -- > B")
    elif ((test_score >= 70)):
        print (f"{test_score} -- > C")
    elif ((test_score >= 60)):
        print (f"{test_score} -- > D")
    elif ((test_score < 0) or (test_score > 100)):
         print (f"Invalid Test Score!")
    else: 
        print (f"{test_score} -- > F")

    #Create a decision structure to determine the season: winter, spring, summer, fall 
    # Ask the user to enter the number of the month and based on the number, determine the season
    # Winter: 12, 1, 2; Spring: 3, 4, 5; Summer: 6, 7, 8; Fall: 9, 10, 11
    #Output/print the season: It is season

    season_no = int(input("What is the number of the month you are in? "))

    if ((season_no == 1) or (season_no == 2) or (season_no == 12)):
        print ("It is Winter")
    elif ((season_no == 3) or (season_no == 4) or (season_no == 5)):
        print ("It is Spring")
    elif ((season_no == 6) or (season_no == 7) or (season_no == 8)):
        print ("It is Summer")
    elif ((season_no == 9) or (season_no == 10) or (season_no == 11)):
        print ("It is Fall")
    else: 
        print ("That is not a valid month")
    
main()
