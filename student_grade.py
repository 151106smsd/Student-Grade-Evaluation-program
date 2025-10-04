# student_grade.py

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

# Take input for 5 subjects
marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

average = sum(marks) 
grade = calculate_grade(average)

print("Marks:", marks)
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
