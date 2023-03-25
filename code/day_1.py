import os 

DATA_PATH="inputs/day_1.txt"

def import_data_to_sublists(filepath: str, sublist_marker: str) -> list:
    with open(filepath, 'r') as file:
        data = [section.split("\n") for section in file.read().split(sublist_marker)]
    return data

def get_max_calories(list_of_rations: list, number_of_places: int = 1) -> list:
    max_rations = [0 for i in range(number_of_places)]
    for i, rations in enumerate(list_of_rations):
        total_cal = sum([int(ration) for ration in rations])
        if total_cal > min(max_rations):
            max_rations.remove(min(max_rations))
            max_rations.append(total_cal)
    return max_rations


def main():
    raw_input = import_data_to_sublists(DATA_PATH, sublist_marker="\n\n")
    # part 1
    max_calories = get_max_calories(raw_input, 1)
    print("The elf with the most calories is carrying " + str(sum(max_calories)) + " calories")
    # part 2
    top_three_calories = get_max_calories(raw_input, 3)
    print("The top " + str(len(top_three_calories)) + " elves with the most calories are carrying " + str(sum(top_three_calories)) + " total calories")


if __name__ == "__main__":
    main()