#Lab 5: Student Performance Functions
#Example: Function that Returns Multiple Values


# Example: returning two values from one function
def min_max(a, b, c):
    smallest = min(a, b, c)      # smallest of the three numbers
    largest = max(a, b, c)       # largest of the three numbers
    return smallest, largest     # returns a tuple of two values
low, high = min_max(4, 9, 2)     # unpack the two returned values
print("Smallest:", low, "Largest:", high)


# Student Task: simple Boolean function

def is_positive(n):
    return n > 0                 # the comparison itself is True or False
print(is_positive(5))
print(is_positive(-3))

#Lab Activity: Student Performance Functions
# Function 1: accepts three marks and returns the average
def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


# Function 2: accepts an average, returns True if it is at least 50, otherwise False
def is_passed(average):
    return average >= 50
# Function 3: accepts an average and returns the grade letter
def get_grade(average):
    if average >= 80:
        return "A"          # 80 or above
    elif average >= 70:
        return "B"          # 70-79
    elif average >= 60:
        return "C"          # 60-69
    elif average >= 50:
        return "D"          # 50-59
    else:
        return "F"          # below 50

# Function 4: accepts the name and three marks, returns average, grade and pass/fail
def student_report(name, m1, m2, m3):
    average = calculate_average(m1, m2, m3)      # uses Function 1
    grade = get_grade(average)                   # uses Function 3
    passed = is_passed(average)                  # uses Function 2
    return average, grade, passed                # three return values

# Function 4: accepts the name and three marks, returns average, grade and pass/fail
def student_report(name, m1, m2, m3):
    average = calculate_average(m1, m2, m3)      # uses Function 1
    grade = get_grade(average)                   # uses Function 3
    passed = is_passed(average)                  # uses Function 2
    return average, grade, passed                # three return values


# ---------------- Main program ----------------
# Take input from the user
student_name = input("Enter student name: ")
mark1 = float(input("Enter marks in subject 1: "))
mark2 = float(input("Enter marks in subject 2: "))
mark3 = float(input("Enter marks in subject 3: "))

# Call student_report() and unpack the three returned values
avg, grade, passed = student_report(student_name, mark1, mark2, mark3)

# Display the complete student report
print()
print("----- Student Report -----")
print("Name:", student_name)
print("Marks:", mark1, mark2, mark3)
print("Average:", f"{avg:.2f}")
print("Grade:", grade)
print("Result:", "Pass" if passed else "Fail")
print("Passed (Boolean):", passed)