max_length = int(input())
for i in range(1, max_length + 1):
    print(i * "*")
for j in range(max_length - 1, 0, -1):
    print(j * "*")