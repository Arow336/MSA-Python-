import datetime
from Student import Student

"""
Function to write an error message to a log file
Input: (string)error message
Output: None
"""

def write_to_error_log(message:str) -> None:
    #open the log file in append mode: error_log.txt
    input_file = open("error_log.txt", "a")
    #write error message to the file in the format
    with open ("error_log.txt", "a") as input_file:
        the_date = datetime.datetime.now()
        input_file.write(f"{the_date}: {message}\n") 
    #Date: message -> 6/24/2025: Error 
    #close the file

    return

"""
Function to return a list of student objects
Input: none 
Output: list of student objects
"""

def load_students() -> list[Student]:
    data_file = open("students.csv", "r" )

    students_list: list[Student] = []
    #create instances of students from information in a file

    #create variable to keep track of line in file that we're reading 
    line_number = 0
    #read file line by line in for loop
    for line_of_data in data_file:
        line_number += 1
        student_data = line_of_data.split(",")
        
        if len(student_data) != 6:
            #write an error messsage to and error log
            write_to_error_log(f"Error on line number: {line_number}, Incorrect data length.")
            continue
        try:
            student = Student(student_data[0],student_data[1],student_data[2],int(student_data[3]),float(student_data[4]),student_data[5])
            students_list.append(student)
        except Exception as err:
            #Write an error message to and error log
            write_to_error_log(f"Error on line number: {line_number}, Incorrect data type")
            continue

    last_name = student_data[1]
    major = student_data[2]
    student_id = student_data[5].strip()


    return students_list
        
"""
Function to convert student objects to student dictionaries
Input: list of student objects
Output: List of student dictionaries
"""
def student_to_dictionary(list_of_students:list[Student]) -> list[dict]:
    #create a list to store the dictionaries in 
    student_dictionary_list = []

    #loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dictionary 
        student_dictionary = {}

        #set the keys and values for the dictionary
        student_dictionary['first name'] = student.get_first_name()
        student_dictionary['last name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class '] = student.get_class_level()
        student_dictionary['ID '] = student.get_ID_no()

        #append the dictionary to the list of dictionaries 
        student_dictionary_list.append(student_dictionary)

    #return the list of dictionaries
    return student_dictionary_list

"""
Function to get a list of student dictionaries
Input: None
Output: List of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    for student_dict in student_dictionaries:
        print(student_dict)

    print (student_dictionaries)
    return student_dictionaries


get_student_dictionaries()