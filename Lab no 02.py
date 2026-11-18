# Lab 2: Student Performance Analyzer
# Example: Grade Using if-elif-else

# Example: pass/fail decision with if-else

marks = 65              

# Check the condition and print the message
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Student Task
# Given a percentage, print its grade using this scale: A = 80 or above, B = 70-79, C = 60-69, D = 50-59, F = below 50.


# Student Task: grade from a percentage

percentage = float(input("Enter percentage: "))   # read the percentage

# Check the highest grade first, then move down
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade) 


# Lab Exercise: Student Performance Analyzer

# 1. Take the student's name
name = input("Enter student name: ")

# 2. Take marks in three subjects (each out of 100)
marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))

# 3. Calculate total marks
total = marks1 + marks2 + marks3

# 4. Calculate percentage (total out of 300)
percentage = total / 300 * 100

# 5. Determine grade using if-elif-else
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# 6. Determine pass/fail status (pass mark is 50%)
if percentage >= 50:
    status = "Pass"
else:
    status = "Fail"
# Display the result
print()
print("----- Student Result -----")
print("Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", f"{percentage:.2f}%")
print("Grade:", grade)
print("Status:", status)