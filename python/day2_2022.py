# Giant Rock-paper-scissors tournament
#
#
# Part 1
def play_game(player, opponent):
    if player == opponent:
        return 'draw'
    elif player == 'rock' and opponent == 'scissor':
        return 'win'
    elif player == 'paper' and opponent == 'rock':
        return 'win'
    elif player == 'scissor' and opponent == 'paper':
        return 'win'
    else:
        return 'lose'


def play_game_with_desired_outcome(opponent, outcome):
    if outcome == 'draw':
        return opponent
    elif outcome == 'win':
        if opponent == 'rock':
            return 'paper'
        elif opponent == 'paper':
            return 'scissor'
        else:
            return 'rock'
    else:
        if opponent == 'rock':
            return 'scissor'
        elif opponent == 'paper':
            return 'rock'
        else:
            return 'paper'


opponent_encryption = {'A': 'rock', 'B': 'paper', 'C': 'scissor'}
player_encryption = {'X': 'rock', 'Y': 'paper', 'Z': 'scissor'}
shape_points = {'rock': 1, 'paper': 2, 'scissor': 3}
outcome_points = {'lose': 0, 'draw': 3, 'win': 6}

test_game = ["A Y", "B X", "C Z"]

games = open("inputs/day2_input.txt", 'r')
test_game = games.readlines()

points = 0
for game in test_game:
    choices = game.strip('\n').split(" ")
    player = player_encryption[choices[1]]
    opponent = opponent_encryption[choices[0]]
    results = play_game(player, opponent)
    points += shape_points[player] + outcome_points[results]

print(points)

# Part 2

desired_outcome = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

points = 0
for game in test_game:
    choices = game.strip('\n').split(" ")
    outcome = desired_outcome[choices[1]]
    opponent = opponent_encryption[choices[0]]
    player = play_game_with_desired_outcome(opponent, outcome)
    points += shape_points[player] + outcome_points[outcome]

print(points)
