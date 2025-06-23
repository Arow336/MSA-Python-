class Student():
    #Define the Student constructor

    def __init__(self,first_name,last_name,major,credit_hours,gpa,ID_no):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__ID_no = ID_no

    #create the getter and setter methods
    def get_first_name(self):
        return self.__first_name 
    
    def set_first_name(self, new_first_name:str):
        self.__first_name = new_first_name

    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, new_last_name:str):
        self.__last_name = new_last_name

    def get_major(self):
        return self.__major
    
    def set_major(self, new_major:str):
        self.__major = new_major

    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours:int):
        self.__credit_hours = new_credit_hours

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self,new_gpa:float):
        self.__gpa = new_gpa

    def get_ID_no(self):
        return self.__ID_no
    
    #create a method to determine the class based on the students credit hours.

    def get_class_level(self,credit_hours:int):
        if (credit_hours >= 0) and (credit_hours <= 30):
            return "Freshman"
        elif (credit_hours >= 31) and (credit_hours <= 60):
            return "Sophomore"
        elif (credit_hours >= 61) and (credit_hours <= 90):
            return "Junior"
        else:
            return "Senior"
        
    def update_credit_hours(self, new_hours):
        self.__credit_hours += new_hours

    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level(self.__credit_hours)} ,Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__ID_no}")
