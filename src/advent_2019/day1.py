import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_total_fuel(array):
    return sum([calculate_fuel(x) for x in array])


def calculate_part2_fuel(mass, total_fuel=0):
    new_mass = calculate_fuel(mass)
    return calculate_part2_fuel(new_mass, total_fuel + new_mass) if new_mass > 0 else total_fuel


def calculate_part2_total_fuel(array):
    return sum([calculate_part2_fuel(x) for x in array])
