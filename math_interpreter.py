#write a program that enables users to do math
# 

def main():
    while True: 
        #prompt the user for an expression
        problem = input("Enter an expression: ")
        #use the split() method to get the parts of the expression
        problem_data = problem.split(" ")
        #check the length of the list returned from .split
       
        if len(problem_data) != 3: 
                print ("ERROR: Enter an expression in the correct format")
                continue
            #if len (list) not = 3, 
            # output Incorrect format message and reprompt(continue)

        #get X and Y and Z values from the list
        value_x = problem_data [0]
        value_y = problem_data [1]
        value_z = problem_data [2]

        try: 
             int_x = int(value_x)
             int_z = int(value_z)
            #and check if X and Z are integers by converting to int()
            #except = 
        except: 
             print("ERROR: Please enter a valid expression: ")
            # output Error message and reprompt

        #Check that operator is +, -, *, /
        if value_y not in ["/", "+", "-", "*"]:      
            #if operator not in [+, -, *, /]
            print ("ERROR: Invalid Operator, Please enter a valid expression: ")
            #output some error message
            # reprompt the user (continue)
            continue
        
        Answer = 0
        #Determine the operation to carry out based on the value of the operator
        #Use if/elif/else block to evaluate the operator and carry out the appropriate operation
        if value_y == "*":
            Answer = int_x * int_z
        elif value_y == "+":
            Answer = int_x + int_z
        elif value_y == "-":
            Answer = int_x * int_z
        elif value_y == "/":
            if int_z == 0:
                  print ("Invalid Divisor (0), Please enter a different number: ")
                  continue
            Answer = int_x / int_z 

        #Output the answer
        print (f"{float(Answer):.2f}")
        break 

main()