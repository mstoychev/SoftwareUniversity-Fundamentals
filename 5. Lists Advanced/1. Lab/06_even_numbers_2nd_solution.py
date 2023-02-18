number_input = list(map(int, input().split(", ")))
found_indices_or_not = map(lambda x: x if number_input[x] % 2 == 0 else "no", range(len(number_input)))
even_indices = list(filter(lambda a: a != "no", found_indices_or_not))
print(even_indices)
