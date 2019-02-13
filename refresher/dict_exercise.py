"""
Create a variable called student with a dictionary.
The dictionary must contain 3 keys: 'name', 'school', and 'grades'.
The values for each must be 'Ose', 'Computing', and a tuple with values 66, 77, 88.
"""

students = { 'name': 'Ose', 'school': 'Computing', 'grades': (66,77,88) }

"""
Assume the argument, data is a dictionary.
Modify the grades variables so it accessees the 'grades' key of the data dictionary.
"""

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)

def average_grade_all_students(students_list): 
    total = 0
    count = 0 
    for student in student_list:
        total += sum(student['grades']) 
        count += len(student['grades'])
    return total / count
