# Ashton Wood
# 03-31-2023
# Student Qualifier
# accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.

students = []

# Get Student Info
while True:
    last_name = input("Enter student's last name (enter ZZZ to quit): ")
    if last_name == 'ZZZ' or last_name == 'zzz':
        break
    
    first_name = input("Enter student's first name: ")
    
    while True:
        try:
            gpa = float(input("Enter student's GPA: "))
            if gpa < 0 or gpa > 4:
                raise ValueError("GPA must be between 0 and 4.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    # add the student data to the list
    students.append((last_name, first_name, gpa))
    
# iterate over the students and test if they qualify for the Dean's List or Honor Roll
for student in students:
    last_name, first_name, gpa = student
    
    # test for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    
    # test for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")