def calculate_result(array, noun, verb):
    finished = False
    current_position = 0
    array[1] = noun
    array[2] = verb
    while finished is False:
        opcode = array[current_position]
        if opcode == 1:
            array[array[current_position + 3]] = array[array[current_position + 1]] + array[array[current_position + 2]]
        elif opcode == 2:
            array[array[current_position + 3]] = array[array[current_position + 1]] * array[array[current_position + 2]]
        elif opcode == 99:
            finished = True
        current_position = current_position + 4
    return array[0]


def calculate_result_part2(array, expected_result):
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = calculate_result(array[:], noun, verb)
            if result == expected_result:
                return 100 * noun + verb
