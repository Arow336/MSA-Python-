from Student import Student

def main():
    data_file = open("students.csv", "r" )

    students_list = []
    #create instances of students from information in a file
    for line_of_data in data_file:
        student_data = line_of_data.split(",")
        
        if len(student_data) != 6:
            continue
        try:
            student = Student(student_data[0],student_data[1],student_data[2],int(student_data[3]),float(student_data[4]),student_data[5])
            students_list.append(student)
        except:
            continue

    for students in students_list:
        students.print_student_data()
        


main()