students = []
courses = []

def add_student():
    student = {}
    student['id'] = input('Enter student ID: ')
    student['name'] = input('Enter student name: ')
    student['age'] = input('Enter student age: ')
    students.append(student)
    print('Student added successfully!')

def delete_student():
    id = input('Enter student ID to delete: ')
    for student in students:
        if student['id'] == id:
            students.remove(student)
            print('Student deleted successfully!')
            return
    print('Student not found')

def edit_student():
    id = input('Enter student ID to edit: ')
    for student in students:
        if student['id'] == id:
            student['name'] = input('Enter new name: ')
            student['age'] = input('Enter new age: ')
            print('Student edited successfully!')
            return
    print('Student not found')

def list_students():
    print('List of students:')
    for student in students:
        print('ID:', student['id'], 'Name:', student['name'], 'Age:', student['age'])

def search_student():
    id = input('Enter student ID to search: ')
    for student in students:
        if student['id'] == id:
            print('ID:', student['id'], 'Name:', student['name'], 'Age:', student['age'])
            return
    print('Student not found')

def add_course():
    course = {}
    course['id'] = input('Enter course ID: ')
    course['name'] = input('Enter course name: ')
    course['units'] = input('Enter course units: ')
    courses.append(course)
    print('Course added successfully!')

def delete_course():
    id = input('Enter course ID to delete: ')
    for course in courses:
        if course['id'] == id:
            courses.remove(course)
            print('Course deleted successfully!')
            return
    print('Course not found')

def edit_course():
    id = input('Enter course ID to edit: ')
    for course in courses:
        if course['id'] == id:
            course['name'] = input('Enter new name: ')
            course['units'] = input('Enter new units: ')
            print('Course edited successfully!')
            return
    print('Course not found')

def list_courses():
    print('List of courses:')
    for course in courses:
        print('ID:', course['id'], 'Name:', course['name'], 'Units:', course['units'])

def search_course():
    id = input('Enter course ID to search: ')
    for course in courses:
        if course['id'] == id:
            print('ID:', course['id'], 'Name:', course['name'], 'Units:', course['units'])
            return
    print('Course not found')

while True:
    print('Welcome to the Student Information System!')
    print('1. Add student')
    print('2. Delete student')
    print('3. Edit student')
    print('4. List students')
    print('5. Search student')
    print('6. Add course')
    print('7. Delete course')
    print('8. Edit course')
    print('9. List courses')
    print('10. Search course')
    print('11. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        edit_student()
    elif choice == 4:
        list_students()
    elif choice

