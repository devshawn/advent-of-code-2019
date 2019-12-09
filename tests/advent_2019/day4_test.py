import pytest

from src.advent_2019 import day4

test_cases_part_1 = [
    (111111, 111111, 1),
    (122345, 122345, 1),
    (223450, 223450, 0),
    (123789, 123789, 0),
    (111111, 111112, 2),
    (123444, 123444, 1),
]

test_cases_part_2 = [
    (112233, 112233, 1),
    (123444, 123444, 0),
    (111122, 111122, 1),
    (111122, 111123, 1)
]


@pytest.mark.parametrize("minimum, maximum, expected", test_cases_part_1)
def test_criteria_one(minimum, maximum, expected):
    result = day4.part_1(minimum, maximum)
    assert result == expected


@pytest.mark.parametrize("minimum, maximum, expected", test_cases_part_2)
def test_criteria_two(minimum, maximum, expected):
    result = day4.part_2(minimum, maximum)
    assert result == expected


def test_part_1():
    result = day4.part_1(134792, 675810)
    assert result == 1955


def test_part_2():
    result = day4.part_2(134792, 675810)
    assert result == 1319
