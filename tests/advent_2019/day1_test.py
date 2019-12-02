import pytest

from src.advent_2019 import day1

input_array = [
    132709,
    102150,
    126463,
    85035,
    77219,
    86458,
    119251,
    121098,
    118730,
    122505,
    127964,
    68004,
    55833,
    77664,
    142865,
    124503,
    115892,
    87236,
    122743,
    127096,
    94893,
    62129,
    56520,
    117000,
    81519,
    121719,
    96291,
    96556,
    79006,
    137122,
    124340,
    125151,
    51603,
    50132,
    67568,
    132599,
    149009,
    60997,
    99382,
    96506,
    57269,
    118133,
    115119,
    126208,
    101098,
    60514,
    146171,
    70314,
    76473,
    51209,
    99190,
    57647,
    126985,
    142055,
    99615,
    146442,
    129520,
    145334,
    57799,
    87148,
    118362,
    80407,
    106449,
    57146,
    129035,
    60156,
    120016,
    147383,
    68819,
    83868,
    81021,
    131594,
    137692,
    86537,
    110709,
    127678,
    106849,
    137640,
    108482,
    131412,
    70331,
    90118,
    117557,
    117347,
    84688,
    108869,
    145359,
    127024,
    100976,
    90419,
    53362,
    106100,
    129474,
    56101,
    99975,
    79211,
    99865,
    121099,
    74511,
    123172
]

example_input_part_1 = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583)
]

example_input_part_2 = [
    (12, 2),
    (1969, 966)
]


# part 1
@pytest.mark.parametrize("test_input, expected", example_input_part_1)
def test_calculate_fuel(test_input, expected):
    assert day1.calculate_fuel(test_input) == expected


def test_calculate_total_fuel():
    assert day1.calculate_total_fuel([12, 14]) == 4


def test_input_part_1():
    assert day1.calculate_total_fuel(input_array) == 3393938


# part 2
@pytest.mark.parametrize("test_input, expected", example_input_part_2)
def test_calculate_part2_fuel_1(test_input, expected):
    assert day1.calculate_part2_fuel(test_input) == expected


def test_input_part_2():
    assert day1.calculate_part2_total_fuel(input_array) == 5088037
