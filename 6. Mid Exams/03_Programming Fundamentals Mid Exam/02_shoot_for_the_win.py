shot_target = list(map(int, input().split()))
command = input()
count = 0
while command != "End":
    index = int(command)
    if 0 <= index <= len(shot_target) - 1:
        count += 1
        value = shot_target[index]
        shot_target[index] = -1
        for i in range(len(shot_target)):
            if shot_target[i] == -1:
                continue
            if shot_target[i] <= value:
                shot_target[i] += value
            else:
                shot_target[i] -= value

    command = input()
shot_target_str = [str(x) for x in shot_target]
result = ' '.join(shot_target_str)
print(f"Shot targets: {count} -> {result}")
