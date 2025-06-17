""""
Function to get valid expression inputs from the user 
Input: None
Outputs: (int)x, (int)y, (string)y
"""
def get_valid_expression_inputs():
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

        if (value_y == "/") and (int_z == 0):
            print("ERROR: Invalid division (can't divide by 0), Enter a valid expression: ")
            continue

        return int_x, value_y, int_z

"""
Function to evaluate an expression
Inputs: X(int), Y(string), X(int)
Output: Answer

"""
def evaluate_expression(int_x:int, value_y:str, int_z:int):
   
    Answer = 0
    #Determine the operation to carry out based on the value of the operator
    #Use if/elif/else block to evaluate the operator and carry out the appropriate operation
    if value_y == "*":
        Answer = int_x * int_z
        return Answer
    elif value_y == "+":
        Answer = int_x + int_z
        return Answer
    elif value_y == "-":
        Answer = int_x * int_z
        return Answer
    elif value_y == "/":
        Answer = int_x / int_z 
        return Answer


def main():
    condition = True
    while condition: 
        #call the get_valid_expression_inputes function to get x,y,z
        x, y, z = get_valid_expression_inputs()

        #Call evaluate_expression to get the answer for the expression
        results = evaluate_expression(x,y,z)
        #print the answer
        print (f"{float(results):.2f}")
        #ask the user if they want to evaluate another expression
        repeat = input("Would you like to rerun the program (y/n)? ")
        #rerun the program if the user wants to continue, otherwise end the program
        if (repeat == "y") or (repeat == "Y"):
            continue
        else:
            break 


main()