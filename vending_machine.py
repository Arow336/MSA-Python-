#Write a program that acts a vending machine for a 50 cent snack 


def main():
    
    #This will loop until the user's amount due is 0
    amount_due = 50 
    condition = True
    while condition: 
        print (f"Amount Due: {amount_due}")
        #print vending machine 
        #use input function to get user input 

        #validate user input with function to make sure it's a correct coin
        coin_no= input("Insert Coin \n")
        if ((coin_no != "1") and (coin_no != "5") and (coin_no != "10") and (coin_no != "25")):
            continue

        coin_no = int(coin_no)


        #Display amount due to the user 
        amount_due = amount_due - coin_no

        #Calculate change owed to the user 

        #Exit condition 
        if (amount_due <= 0):
            condition = False 

        
    print (f"Change Owed: {amount_due * -1}")
            
            




main()