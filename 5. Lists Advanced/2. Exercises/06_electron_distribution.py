electrons = int(input())

shells = []
n = 0
while electrons > 0:
    n += 1
    max_electrons = 2 * (n * n)

    if max_electrons > electrons:
        shells.append(electrons)
        electrons = 0
        break

    shells.append(max_electrons)
    electrons -= max_electrons

print(shells)