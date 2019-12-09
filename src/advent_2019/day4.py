import itertools
from collections import Counter


def part_1(start, end):
    counter = itertools.count(0)
    [(next(counter), i) for i in range(start, end + 1) if len(str(i)) != len(set(str(i))) and sorted(str(i)) == list((str(i)))]
    return next(counter)


def part_2(start, end):
    counter = itertools.count(0)
    [(next(counter), i) for i in range(start, end + 1) if
     len(str(i)) != len(set(str(i))) and sorted(str(i)) == list((str(i))) and 2 in Counter(sorted(str(i))).values()]
    return next(counter)


print(part_1(134792, 675810))
print(part_2(134792, 675810))
