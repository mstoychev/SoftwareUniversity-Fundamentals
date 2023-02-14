N = int(input())     #number of snowballs
best_score = float("-inf")       # -sys.maxsize ; even 0 it´s ok for the exercise
output = ""

for idx in range(N):
    weight = int(input())
    time = int(input())
    quality = int(input())
    formula = (weight // time) ** quality

    if formula > best_score:
        best_score = formula
        output = f"{weight} : {time} = {best_score} ({quality})"

print(output)

