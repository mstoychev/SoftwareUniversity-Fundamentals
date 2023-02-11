command = input()
coffees = 0
while command != "END":
    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        coffees += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        coffees += 2
    command = input()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
