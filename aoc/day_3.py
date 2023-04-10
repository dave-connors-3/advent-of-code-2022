import os 
from string import ascii_letters
import more_itertools as mit
from typing import List

DATA_PATH="inputs/day_3.txt"

def get_rucksacks():
    with open(DATA_PATH, 'r') as file:
        return file.read().splitlines()

def find_error_item(rucksack):
    compartment_1, compartment_2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    return set(compartment_1).intersection(compartment_2).pop()

def find_badge_item(rucksack_group):
    ruck_1 = rucksack_group[0]
    ruck_2 = rucksack_group[1]
    ruck_3 = rucksack_group[2]
    return set(ruck_1).intersection(ruck_2).intersection(ruck_3).pop()

def find_badge_groups(rucksacks):
    return list(mit.chunked(rucksacks, 3))

def get_item_value(rucksack_item):
    return ascii_letters.index(rucksack_item) + 1

def get_error_priority(list_of_rucksacks):
    return sum([get_item_value(find_error_item(rucksack)) for rucksack in list_of_rucksacks])

def get_badge_priority(list_of_rucksacks):
    badge_grouped = find_badge_groups(list_of_rucksacks)
    return sum([get_item_value(find_badge_item(rucksack_group)) for rucksack_group in badge_grouped])

def main():
    all_rucksacks = get_rucksacks()
    print("Total error value: " + str(get_error_priority(all_rucksacks)))
    print("Total badge value: " + str(get_badge_priority(all_rucksacks)))

if __name__ == "__main__":
    main()