from aoc import day_3
import pytest

test_lines = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def test__error_sum():
    test_rucksacks = test_lines.split('\n')
    assert (day_3.get_error_priority(test_rucksacks)) == 157

def test__badge_sum():
    test_rucksacks = test_lines.split('\n')
    assert (day_3.get_badge_priority(test_rucksacks)) == 70


if __name__ == '__main__':
    test_rucksacks = test_lines.split('\n')
    print(test_rucksacks)
