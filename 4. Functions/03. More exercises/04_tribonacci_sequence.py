def tribonacci_sequence(num):
    sequence = []
    for i in range(num):
        if len(sequence) < 2:
            x = 1
            sequence.append(x)
        elif len(sequence) == 2:
            x = sequence[-1] + sequence[-2]
            sequence.append(x)
        else:
            x = sequence[-1] + sequence[-2] + sequence[-3]
            sequence.append(x)

    sequence_str = [str(j) for j in sequence]  #transform int_list into str_list for use join() method
    return print(" ".join(sequence_str))


number = int(input())
tribonacci_sequence(number)
