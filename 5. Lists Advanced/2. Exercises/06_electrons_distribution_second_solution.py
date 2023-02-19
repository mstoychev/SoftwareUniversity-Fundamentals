def max_electrons_per_shelL(n):
    maximum_electrons = 2 * (n ** 2)
    return maximum_electrons


electron_maximus = int(input())
current_electron = 1
max_per_shell = 0
result = []
while electron_maximus > 0:
    max_per_shell = max_electrons_per_shelL(current_electron)
    if electron_maximus < max_per_shell:
        result.append(electron_maximus)
        electron_maximus = 0
        break
    result.append(max_per_shell)
    electron_maximus -= max_per_shell
    current_electron += 1

print(result)