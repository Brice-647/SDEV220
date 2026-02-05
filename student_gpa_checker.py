# Name: Brice Puthoff
# File Name: student_gpa_checker.py
# Description: This program accepts student names and GPAs and determines
#              whether each student qualifies for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

    if last_name == "ZZZ":
        print("Program terminated.")
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for honors.")

    print()
