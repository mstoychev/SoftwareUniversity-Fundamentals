students_dict = {}
command = input().split(":")
while len(command) > 1:
    name, id, course = command[0], command[1], command[2]
    if course not in students_dict.keys():
        students_dict[course] = []
    students_dict[course].append(f"{name} - {id}")
    command = input().split(":")

searched_course = command[0].replace("_", " ")
for student in students_dict[searched_course]:
    print(student)
