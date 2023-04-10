import os 

DATA_PATH="inputs/day_4.txt"

def get_assignment_lines():
    with open(DATA_PATH, 'r') as file:
        return file.read().splitlines()

def get_sections_list(assignment_row):
    assignments = assignment_row.split(',')
    full_assignment = []
    for assignment in assignments:
        start = int(assignment.split('-')[0])
        stop = int(assignment.split('-')[1]) + 1
        full_assignment.append(list(range(start, stop)))
    return full_assignment

def is_full_overlap(assignment_pair):
    assignment_1 = assignment_pair[0]
    assignment_2 = assignment_pair[1]
    return all(i in assignment_1 for i in assignment_2) or all(i in assignment_2 for i in assignment_1)

def is_partial_overlap(assignment_pair):
    assignment_1 = assignment_pair[0]
    assignment_2 = assignment_pair[1]
    return any(i in assignment_1 for i in assignment_2) or any(i in assignment_2 for i in assignment_1)

def get_total_overlaps(assignment_lines):
    all_sections = [get_sections_list(item) for item in assignment_lines]
    return sum([is_full_overlap(assigment_pair) for assigment_pair in all_sections])

def get_partial_overlaps(assignment_lines):
    all_sections = [get_sections_list(item) for item in assignment_lines]
    return sum([is_partial_overlap(assigment_pair) for assigment_pair in all_sections])

if __name__ == '__main__':
    data = get_assignment_lines()
    print("total overlapping assigments: " + str(get_total_overlaps(data)))
    print("total partially overlapping assigments: " + str(get_partial_overlaps(data)))