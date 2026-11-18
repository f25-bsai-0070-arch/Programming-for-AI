# Lab 3: Loops: Student Records with Sentinel
# Example 1: while loop with a sentinel
# A sentinel is a special value (here -1) that tells the loop to stop.

# Example 1: while loop that stops at the sentinel -1

number = int(input("Enter a number (-1 to stop): "))   # first value
count = 0                                              # how many numbers were entered
# Keep looping until the user enters the sentinel
while number != -1:
    count += 1                                         # augmented assignment: count = count + 1
    number = int(input("Enter a number (-1 to stop): "))
print("You entered", count, "numbers")

# Example 2: for loop with range() and a nested loop
# Example 2: for loop with range() and a nested loop

# 'i' is the target variable that takes the values 1, 2, 3
for i in range(1, 4):
    # inner (nested) loop runs fully for every value of i
    for j in range(1, 4):
        print(i * j, end="\\t")     # print on the same line, separated by a tab
    print()                        # move to the next line after each row

#Student Tasks
#Task 1: Use a for loop to print the numbers 1 to 10 and their sum (use +=).
#Task 2: Print the multiplication table of 5.

# Student Task 1: sum of 1 to 10 using augmented assignment

total = 0
for n in range(1, 11):     # n takes the values 1..10
    total += n             # add n to the running total
print("Sum of 1 to 10 =", total)
# Student Task 2: multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

#Lab Exercise: Student Marks with Sentinel  
subjects = ["Programming", "Mathematics", "Artificial Intelligence"]   # the three subjects

student_count = 0          # total number of students entered
grand_total = 0            # sum of marks of ALL students (for the overall average)

# Ask for the first student; -1 is the sentinel that stops the loop
name = input("Enter student name (-1 to stop): ")

# 1. while loop: keeps accepting students until the sentinel -1 is entered
while name != "-1":
    total = 0              # total marks of the current student (reset for each student)

    # 2. for loop with range() reads the marks of the three subjects
    #    'i' is the target variable that moves through positions 0, 1, 2
    for i in range(3):
        subject = subjects[i]                                  # subject at position i
        marks = int(input(f"Enter {subject} marks: "))
        # keep asking until the marks are between 0 and 100
        while marks < 0 or marks > 100:
            print("Invalid marks! Enter a value between 0 and 100.")
            marks = int(input(f"Enter {subject} marks: "))
        total += marks                                         # 4. augmented assignment

    average = total / 3                                        # average of this student

    # 5. Display this student's total and average
    print()
    print("----- Result for", name, "-----")
    print("Total Marks:", total)
    print("Average Marks:", f"{average:.2f}")

    # 6. Nested loop: multiplication table from 1 to 5
    print("Multiplication table (1 to 5) for", name)
    for row in range(1, 6):              # outer loop: the rows
        for col in range(1, 6):          # inner loop: the columns
            print(row * col, end="\\t")
        print()                          # new line after each row
    print()

        # Update the counters for the final summary
    student_count += 1
    grand_total += total

    # Ask for the next student (the loop ends if the answer is -1)
    name = input("Enter student name (-1 to stop): ")

# 7. Final summary
print()
print("===== Final Summary =====")
print("Total number of students:", student_count)
if student_count > 0:
    # every student has 3 subjects, so total marks are divided by student_count * 3
    overall_average = grand_total / (student_count * 3)
    print("Overall average:", f"{overall_average:.2f}")
else:
    print("No students were entered.")
