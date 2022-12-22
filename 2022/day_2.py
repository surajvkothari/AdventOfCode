# Advent of code 2022
# Day 2

def get_data():
    with open("day_2_data.txt") as f:
        opponent_letters, player_letters = [], []
        for line in f:
            # Get moves
            opponent, player = line.split()

            opponent_letters.append(opponent)
            player_letters.append(player)

    return opponent_letters, player_letters


def decode_player(letter):
    decoding = {'X': "Rock", 'Y': "Paper", 'Z': "Scissors"}
    return decoding[letter]

def decode_opponent(letter):
    decoding = {'A': "Rock", 'B': "Paper", 'C': "Scissors"}
    return decoding[letter]


def get_move(opponent_shape, player_letter):
    if player_letter == 'X':
        # Lose
        if opponent_shape == "Rock":
            return "Scissors"
        elif opponent_shape == "Paper":
            return "Rock"
        elif opponent_shape == "Scissors":
            return "Paper"

    elif player_letter == 'Y':
        # Draw
        return opponent_shape

    elif player_letter == 'Z':
        # Win
        if opponent_shape == "Rock":
            return "Paper"
        elif opponent_shape == "Paper":
            return "Scissors"
        elif opponent_shape == "Scissors":
            return "Rock"


def get_result(player_shapes, opponent_shapes):
    results = []
    for player, opponent in zip(player_shapes, opponent_shapes):
        if player == opponent:
            results.append("D")
        elif (player == "Rock" and opponent == "Scissors") or \
             (player == "Paper" and opponent == "Rock") or \
             (player == "Scissors" and opponent == "Paper"):

            results.append("W")
        else:
            results.append("L")

    return results

def get_score(shape, result):
    shape_scores = {"Rock": 1, "Paper": 2, "Scissors": 3}
    outcomes = {"W": 6, "D": 3, "L": 0}

    return shape_scores[shape] + outcomes[result]


def part1(opponent_letters, player_letters):
    player_shapes = list(map(decode_player, player_letters))
    opponent_shapes = list(map(decode_opponent, opponent_letters))

    results = get_result(player_shapes, opponent_shapes)

    total_score = 0
    for shape, results in zip(player_shapes, results):
        total_score += get_score(shape, results)

    print("Part 1:", total_score)


def part2(opponent_letters, player_letters):
    opponent_shapes = list(map(decode_opponent, opponent_letters))

    # Get the player's shape based on the opponent's shape and the player's letter
    player_shapes = list(map(get_move, opponent_shapes, player_letters))

    results = get_result(player_shapes, opponent_shapes)

    total_score = 0
    for shape, results in zip(player_shapes, results):
        total_score += get_score(shape, results)

    print("Part 2:", total_score)
    

opponent_letters, player_letters = get_data()
part1(opponent_letters, player_letters)
part2(opponent_letters, player_letters)
