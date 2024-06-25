import unittest
import timeit
from star_rail_parser import RelicStat


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass
        # self.assertEqual(True, False)  # add assertion here


relic = RelicStat('ATK', 100, False, 1, 10)


# if __name__ == '__main__':
#     unittest.main()
def test_direct():
    return relic.type, relic.value, relic.isPercent, relic.count, relic.step


# Test dictionary access
def test_dict():
    d = relic.__dict__
    return d['type'], d['value'], d['isPercent'], d['count'], d['step']


# Benchmark
# print("Direct access:", timeit.timeit(test_direct, number=1000000))
# print("Dict access:", timeit.timeit(test_dict, number=1000000))

stats_dict = {}

# List of objects (assuming they're instances of RelicStat)
relic_list = [
    RelicStat('HP', 100, False),
    RelicStat('ATK', 50, False),
    RelicStat('DEF', 75, False),
    RelicStat('HP', 50, False),  # Another HP stat
    RelicStat('CRIT', 10, True)  # A new stat type
]

# Iterate over the list of objects
for relic in relic_list:
    if relic.type in stats_dict:
        # If the key exists, add to its value
        stats_dict[relic.type] += relic.value
    else:
        # If the key doesn't exist, create it
        stats_dict[relic.type] = relic.value

# Print the updated dictionary
print(stats_dict)
