course_dict = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course = command[0]
    name = command[1]
    if course not in course_dict:
        course_dict[course] = [name]
    else:
        course_dict[course].append(name)

for key, value in course_dict.items():
    print(f"{key}: {len(value)}")
    for element in value:
        print(f"-- {element}")