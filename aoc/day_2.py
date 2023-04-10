import os 

DATA_PATH="inputs/day_2.txt"
TEST_RUN = False
OUTCOME_MAP = {
    "A" : {
        "throws" : "rock",
        "loses_to" : "Y",
        "thrown_by" : "them",
        "outcome" : "unknown",
        "throw_points" : 1
    },
    "B" : {
        "throws" : "paper",
        "loses_to" : "Z",
        "thrown_by" : "them",
        "outcome" : "unknown",
        "throw_points" : 2
    },
    "C" : {
        "throws" : "scissors",
        "loses_to" : "X",
        "thrown_by" : "them",
        "outcome" : "unknown",
        "throw_points" : 3
    },
    "X" : {
        "throws" : "rock",
        "loses_to" : "B",
        "thrown_by" : "me",
        "outcome" : "lose",
        "throw_points" : 1
    },
    "Y" : {
        "throws" : "paper",
        "loses_to" : "C",
        "thrown_by" : "me",
        "outcome" : "draw",
        "throw_points" : 2
    },
    "Z" : {
        "throws" : "scissors",
        "loses_to" : "A",
        "thrown_by" : "me",
        "outcome" : "win",
        "throw_points" : 3
    },

}

def split_data_to_games(filepath=None, str_obj=None):
    if filepath:
        with open(filepath, 'r') as file:
            raw_data = file.read()
    elif str_obj:
        raw_data = str_obj
    data = [section.split(" ") for section in raw_data.splitlines()]
    return data

def score_game_outcome(game: list, version: int = 1):
    opponent_throw = game[0]
    if version == 1:
        my_throw = game[1]
    else: 
        my_throw = resolve_throw_by_outcome(game)
    my_throw_points = OUTCOME_MAP.get(my_throw).get("throw_points")
    if OUTCOME_MAP.get(my_throw).get("throws") == OUTCOME_MAP.get(opponent_throw).get("throws"):
        # print("Draw!")
        outcome_points = 3
    elif my_throw == OUTCOME_MAP.get(opponent_throw).get("loses_to"):
        # print("You win!")
        outcome_points = 6
    else: 
        # print("You Lose")
        outcome_points = 0

    total_game_points = my_throw_points + outcome_points
    # print("Total points for the game: " + str(total_game_points))
    return total_game_points

def resolve_throw_by_outcome(game):
    """
    return X, Y, or Z based on the necessary outcome of the game
    """
    opponent_throw = game[0]
    my_outcome = game[1]
    opponent_data = OUTCOME_MAP.get(opponent_throw)
    outcome = OUTCOME_MAP.get(my_outcome).get("outcome")
    win_throw = opponent_data.get("loses_to")
    draw_throw = list({k: v for k, v in OUTCOME_MAP.items() if (v["throws"] == opponent_data["throws"] and v["thrown_by"] == "me")}.keys())[0]
    lose_throw = list({k: v for k, v in OUTCOME_MAP.items() if (k not in [win_throw, draw_throw] and v["thrown_by"] == "me")}.keys())[0]

    if outcome == "win":
        return win_throw
    elif outcome == "lose":
        return lose_throw
    else:
        return draw_throw


def main():
    
    if TEST_RUN:
        game_text = """A Y
B X
C Z
"""
        games = split_data_to_games(str_obj=game_text)
    else:
        games = split_data_to_games(filepath=DATA_PATH)
    total_score = 0
    for game in games:
        total_score += score_game_outcome(game)
    print("Total Score part one: " + str(total_score))
    
    total_score_v2 = 0
    for game in games:
        total_score_v2 += score_game_outcome(game, version=2)
    print("Total Score part two: " + str(total_score_v2))

if __name__ == "__main__":
    main()