population = list(map(int, input().split(", ")))
min_wealth = int(input())
average = sum(population) / len(population)

if min_wealth > average:
    print("No equal distribution possible")
    exit()

for i in range(len(population)):
    num = population[i]
    if num < min_wealth:
        result = min_wealth - num
        max_number = max(population)
        index_max_num = population.index(max_number)
        reduced = max_number - result
        population[i] = min_wealth
        population[index_max_num] = reduced
print(population)