n = int(input())
for _ in range(n):
    string = input()
    for ch in string:
        if ch == "," or ch == "." or ch == "_":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
