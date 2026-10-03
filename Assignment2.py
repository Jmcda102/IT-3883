# Program Name: Assignment2.py
# Course: IT3883/
# Student Name: Julien McDaniel
# Assignment Number: 2
# Due Date: 10/2/2026
# Purpose: This program reads student names and six grades from a file.
# It calculates each student's final average and displays the
# students in descending order by average grade.
# Resources Used: Course materials and W3School.

# Store student names and averages in a list.
students = []

# Input user file name.
file_name = "Assignment2input.txt"

# Open and read the input file.
with open(file_name, "r") as file:
    # Read one student line at a time.
    for line in file:
        data = line.split()

        # Get the student's name and six scores.
        name = data[0]
        scores = data[1:]

        # Convert the score strings to numbers and find the average.
        total = 0
        for score in scores:
            total += float(score)

        average = total / 6

        # Add the student's name and average to the list.
        students.append([name, average])

# Sort the list by average from highest to lowest.
students.sort(key=lambda student: student[1], reverse=True)

# Print each student's name and final average.
for student in students:
    print(student[0], format(student[1], ".2f"))
