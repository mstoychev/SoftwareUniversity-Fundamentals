command = input()
school_information = {}
while command != "end":
    command = command.split(" : ")
    language_name = command[0]
    student_name = command[1]
    school_information[language_name] = school_information.get(language_name, {})
    school_information[language_name][student_name] = student_name
    command = input()

for course in school_information:
    print(f"{course}: {len(school_information[course])}")
    for key, value in school_information[course].items():
        print(f"-- {value}")