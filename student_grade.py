# student_grade.py

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

# Take input
marks = int(input("Enter the marks of the student: "))
grade = calculate_grade(marks)

print(f"Marks: {marks}")
print(f"Grade: {grade}")
