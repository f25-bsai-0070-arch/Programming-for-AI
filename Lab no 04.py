#Lab 4: Functions: Student Performance Analyzer
#Example 1: Function with Parameters and Return Value
# Example 1: a function with parameters and a return value
def add(a, b):              # a and b are parameters
    result = a + b          # 'result' is a LOCAL variable (exists only inside the function)
    return result           # send the value back to the caller
print(add(10, 20))          # 10 and 20 are arguments

#Example 2: Global Constant
PASS_MARKS = 50             # constant (written in capital letters by convention)
def check(percentage):
    # functions can read the global constant
    if percentage >= PASS_MARKS:
        return "Pass"
    return "Fail"
print(check(65))
print(check(40))

#Student Tasks
#Task 1: Write a function square(n) that returns the square of a number.
#Task 2: Write a function is_even(n) that returns True for even numbers.
# Student Task 1 and 2
def square(n):
    return n * n            # return the square of n
def is_even(n):
    return n % 2 == 0       # True if the remainder after dividing by 2 is 0
print(square(7))
print(is_even(10), is_even(7))

#Lab Exercise: Student Performance Analyzer (with Functions)
# Global constant: the minimum percentage needed to pass
PASS_MARKS = 50

# Total number of subjects and the maximum marks of each subject
SUBJECTS = ["Subject 1", "Subject 2", "Subject 3"]
MAX_MARKS = 100


def calculate_total(m1, m2, m3):
    # Add the three marks and return the total
    total = m1 + m2 + m3                     # local variable
    return total


def calculate_percentage(total, num_subjects, max_marks):
    # Percentage = total / (number of subjects * max marks) * 100
    maximum = num_subjects * max_marks       # local variable: highest possible total
    percentage = total / maximum * 100
    return percentage


def determine_grade(percentage):
    # Decide the grade using if-elif-else
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
def determine_status(percentage):
    # Use the global constant PASS_MARKS to decide Pass or Fail
    if percentage >= PASS_MARKS:
        return "Pass"
    else:
        return "Fail"


def highest_subject(names, marks):
    # Challenge: find the subject with the highest marks
    best_index = 0                           # assume the first subject is the highest
    for i in range(1, len(marks)):
        if marks[i] > marks[best_index]:     # a higher mark was found
            best_index = i
    return names[best_index], marks[best_index]


def display_result(name, marks, total, percentage, grade, status):
    # Show the complete result (all values come in as arguments)
    best_name, best_marks = highest_subject(SUBJECTS, marks)
    print()
    print("----- Student Performance Report -----")
    print("Name:", name)
    for i in range(len(marks)):
        print(f"{SUBJECTS[i]}: {marks[i]}")
    print("Total Marks:", total, "/", len(marks) * MAX_MARKS)
    print("Percentage:", f"{percentage:.2f}%")
    print("Grade:", grade)
    print("Status:", status)
    print("Highest Scoring Subject:", best_name, "with", best_marks, "marks")
def main():
    # 1. Ask for the student's name
    name = input("Enter student name: ")

    # 2. Ask for marks in three subjects
    m1 = float(input("Enter marks in Subject 1: "))
    m2 = float(input("Enter marks in Subject 2: "))
    m3 = float(input("Enter marks in Subject 3: "))

    # 3-6. Call the functions, passing data between them as arguments
    total = calculate_total(m1, m2, m3)
    percentage = calculate_percentage(total, len(SUBJECTS), MAX_MARKS)
    grade = determine_grade(percentage)
    status = determine_status(percentage)
    display_result(name, [m1, m2, m3], total, percentage, grade, status)


# Start the program
main()