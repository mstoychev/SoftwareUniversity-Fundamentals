n_rows = int(input())
student_grades = {}

for _ in range(n_rows):
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = grade
    else:
        student_grades[name] = (student_grades[name] + grade) / 2  #average score

for key, value in student_grades.items():
    if value >= 4.5:
        print(f"{key} -> {value:.2f}")