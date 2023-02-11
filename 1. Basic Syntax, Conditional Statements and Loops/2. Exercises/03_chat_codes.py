n_lines = int(input())
for _ in range(n_lines):
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command < 88 and command != 86:
        print("GREAT!")
    else:
        print("Bye.")
