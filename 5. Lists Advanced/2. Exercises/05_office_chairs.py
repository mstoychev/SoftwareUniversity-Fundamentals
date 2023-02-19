rooms = int(input())
final_list = []
for room in range(1, rooms + 1):
    current_room = input().split(" ")
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    difference = chairs - visitors
    final_list.append(difference)

free_chairs = sum(final_list)
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
else:
    for element in final_list:
        if element <= 0:
            print(f"{abs(element)} more chairs needed in room {final_list.index(element) + 1}")
