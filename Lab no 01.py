# Lab No 1: Student Information Program
# Topics: Variables, Input, Arithmetic, and Loops

# Example 1: Variables and Arithmetic

# Store three marks in variables
programming = 80
mathematics = 75
ai = 90

# Calculate total and average
total = programming + mathematics + ai
average = total / 3

# Display results
print("Total Marks:", total)
print("Average Marks:", f"{average:.2f}")


# Example 2: Taking Input from the User

age = int(input("Enter your age: "))
print("Next year you will be", age + 1)

# Task 1: Sum, Difference, and Product

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

# Task 2: Student Greeting

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name + "! You are", age, "years old.")

# Lab Exercise: Student Information

# Take input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
programming = int(input("Enter Programming marks: "))
mathematics = int(input("Enter Mathematics marks: "))
ai = int(input("Enter AI marks: "))

# Calculate total and average
total = programming + mathematics + ai
average = total / 3

# Display student information
print("\n----- Student Information -----")
print("Name:", name)
print("Age:", age)
print("Programming Marks:", programming)
print("Mathematics Marks:", mathematics)
print("AI Marks:", ai)
print("Total Marks:", total)
print("Average Marks:", f"{average:.2f}")

# Challenge Task: 

# Take student information
name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
courses = int(input("Enter Number of Courses: "))

# Read marks using a loop
total = 0

for i in range(1, courses + 1):
    marks = int(input(f"Enter Marks in Course {i}: "))
    total += marks

# Calculate results
average = total / courses
age_after_5 = age + 5
bonus_average = (total + 5 * courses) / courses

# Display challenge results
print("\n----- Challenge Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", f"{average:.2f}")
print("Age after 5 years:", age_after_5)
print("Average after 5 bonus marks in each subject:", f"{bonus_average:.2f}")
