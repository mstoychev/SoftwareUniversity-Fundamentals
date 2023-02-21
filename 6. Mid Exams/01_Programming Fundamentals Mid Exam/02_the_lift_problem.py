people = int(input())
wagons = list(map(int, input().split()))

for i in range(len(wagons)):
    max_people_per_wagon = min(4 - wagons[i], people)
    wagons[i] += max_people_per_wagon
    people -= max_people_per_wagon

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif any(wagon < 4 for wagon in wagons):
    print("The lift has empty spots!")
print(*wagons)




