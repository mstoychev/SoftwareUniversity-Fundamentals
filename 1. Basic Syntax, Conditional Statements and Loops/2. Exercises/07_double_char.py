word = input()
while word != "End":
    duplicate = ""
    if word == "SoftUni":
        pass
    else:
        for ch in word:
            double_char = ch * 2
            duplicate += double_char
        print(duplicate)
    word = input()
