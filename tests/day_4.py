from aoc import day_4

test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

assignment_lines = test_input.splitlines()

def test__count_total_overlaps():
    assert day_4.get_total_overlaps(assignment_lines) == 2

def test__count_partial_overlaps():
    assert day_4.get_partial_overlaps(assignment_lines) == 4