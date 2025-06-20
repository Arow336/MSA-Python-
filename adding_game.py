#Write a program that prompts the user to perform a series of addition problems
# get the inputs from the user
import random
"""
Function to get the difficulty level from the user
Input: None
Output: Returns difficulty level to main
"""
def get_difficulty_level():
    while True:
        #prompts the user till valid input is gotten
        try: 
            #prompts the user for difficulty level
            level = int(input("Enter Level 1,2 3: "))
            if level in [1,2,3]:
                return level
            else:
                print("Error: Invalid Input!\n")
                continue

        except: 
            print("Error: Invalid Input!\n")

"""
Function to get the number of questions the user wants to be asked
Input: None
Output: Returns number of questions to be asked
"""
def get_number_of_questions():
    range_object = range(3,11)
    question_range = list(range_object)
    while True:
        #prompts the user until valid input is gotten
        try:
            #prompts the user for number of questions
            number = int(input("\nEnter number of questions to ask: 3 to 10: "))
            if number in question_range:
                return number
            else:
                print("ERROR: Please enter an integer value between 3 and 10!")  
                continue      
        except:
            print("ERROR: Please enter an integer value between 3 and 10!")



def main():
    #call the get_difficulty_level function to get the difficulty level of the user
    difficulty = get_difficulty_level()

    #call the get_number_of_questions function to get the amount of questions to be asked
    number_of_questions = get_number_of_questions()
    number_generator = random.Random()
    count = 0
    #generates questions for difficulty level 1
    for amount in range(number_of_questions):

        if difficulty == 1:      
            value_x = number_generator.randint(0,9)
            value_y = number_generator.randint(0,9)
        #generates questions for difficulty level 2
        elif difficulty == 2:    
            value_x = number_generator.randint(10,99)
            value_y = number_generator.randint(10,99)
        #generates questions for difficulty level 3
        elif difficulty == 3:
            value_x = number_generator.randint(100,999)
            value_y = number_generator.randint(100,999)


        right_answer = value_x + value_y
        tries = 0 
        for value in range(3):
            try: 
                answer = int(input(f"{value_x} + {value_y} = "))
                if answer != right_answer:
                    print("WRONG!!!")
                    tries += 1
                    continue
                else:
                    print("CORRECT!!!")
                    count += 1
                    break
            except:
                print("Invalid Input!!! ")
                continue
        
        if tries == 3:
            print(f"Correct Answer: {value_x} + {value_y} = {right_answer}")

    print(f"You got {count} out of {number_of_questions} correct: {count/number_of_questions * 100:.2f}%")

main()