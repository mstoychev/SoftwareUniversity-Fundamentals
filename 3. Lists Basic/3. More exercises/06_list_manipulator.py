list_int = [int(j) for j in input().split()]
manipulated_list = []

command = input()
while command != "end":
    command_list = command.split(" ")
    name = command_list[0]
    action = command_list[1]

    if name == "exchange":
        if 0 <= int(action) <= len(list_int) - 1:
            manipulated_list = list_int[int(action)::]
            start_list = list_int[:int(action)]
            for element in start_list:
                manipulated_list.append(element)
            #print(manipulated_list)
        else:
            print("Invalid index")

    elif name == "max":
        max_num_even = 0
        max_num_odd = 0
        if action == "even":
            idx = 0
            for i in range(len(manipulated_list)):
                if manipulated_list[i] % 2 == 0 and manipulated_list[i] > max_num_even:
                    max_num_even = manipulated_list[i]
                    idx = i
            if max_num_even != 0:
                print(idx)

        elif action == "odd":
            idx = 0
            for i in range(len(manipulated_list)):
                if manipulated_list[i] % 2 == 1 and manipulated_list[i] > max_num_odd:
                    max_num_odd = manipulated_list[i]
                    idx = i
            if max_num_odd != 0:
                print(idx)

    elif name == "min":
        pass
    elif name == "first":
        pass
    elif name == "last":
        pass

    command = input()
