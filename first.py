# Print hello world to console 

print ("Hello World!")

# create a variable to store my name
first_name = "Aasiyah"

# print My name is Aasiyah 
print ("My name is", first_name)

#create a variable to store my last name
last_name = "Arowogbadamu"

#Write a statement to display "My full name is first name, last name" 
print ("My full name is", first_name, last_name, sep = "---")

#create variables to store your age, height, weight, and assign them values

age = 16
height = 170.18
weight = 150 

#print a sentence with age, weight, and height

print (f"My name is {first_name} {last_name}\nI am {age} years old and I weigh {weight} lbs")

#get and print the date type for age, weight, and height
print (type (age))
print (type (weight))
print (type (height))

#write 3 print statements using string interpolation (fstring) to print descriptive sentences for 
#the data types 

#Variable age is an int

print (f"Variable age is a {type(age)}\nVariable height is a {type(height)}\nVariable weight is a {type (weight)}")

number_1 = 5
number_2 = 7 

total = number_1 + number_2
print (f"Total: {total}")

number_1 = "5"
number_2 = "7" 

total = number_1 + number_2
print (f"Total: {total}")