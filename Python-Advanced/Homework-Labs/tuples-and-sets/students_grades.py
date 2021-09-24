def calculate_average(list_of_grades):
    return sum(list_of_grades) / len(list_of_grades)


n = int(input())

student_grades = {}

for _ in range(n):
    student, grade_string = input().split()
    grade = float(grade_string)
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

for student, grades in student_grades.items():
    average_grade = calculate_average(grades)
    # we need to print the grades with :.2f too
    grades_str = [str(f'{x:.2f}') for x in grades]
    print(f'{student} -> {" ".join(grades_str)} (avg: {average_grade:.2f})')
