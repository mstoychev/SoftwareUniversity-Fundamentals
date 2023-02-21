population = [int(n) for n in input().split(", ")]
min_wealth = int(input())

distribution = True
for ind, num in enumerate(population):
    if num < min_wealth:
        result = min_wealth - num
        max_number = max(population)
        index_max_num = population.index(max_number)
        changed_max = max_number - result
        if changed_max >= min_wealth:
            population[ind] = min_wealth
            population[index_max_num] = max_number - result
        else:
            distribution = False
            print("No equal distribution possible")
            break
    else:
        population[ind] = num

if distribution:
    print(population)