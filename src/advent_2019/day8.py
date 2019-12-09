def calculate_part_1(input, width, height):
    n = width * height
    layers = [input[i:i + n] for i in range(0, len(input), n)]
    counts = [item.count("0") for item in layers]
    layer = layers[counts.index(min(counts))]
    return layer.count("1") * layer.count("2")


def calculate_part_2(input, width, height):
    n = width * height
    layers = [input[i:i + n] for i in range(0, len(input), n)]
    result = "".join([next(iter([item[i] for item in layers if int(item[i]) is not 2]), 2) for i in range(0, n)])
    result_string = result.replace("0", " ").replace("1", "█")
    return "\n".join([result_string[i:i + width] for i in range(0, len(result_string), width)])
