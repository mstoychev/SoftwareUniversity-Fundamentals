notes = [0] * 10  # The importance value will always be an integer between 1 and 10 (inclusive)
while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)  #remove the zero from the list by index (priority) and insert the note in its place
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)

