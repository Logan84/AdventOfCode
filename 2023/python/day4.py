point_map = {}

def part1(data):
    global point_map
    points = 0
    for i, card in enumerate(data):
        colon_index = card.find(":")
        game = card[colon_index+1:]
        game = game.lstrip(" ")
        game = game.strip("\n").split(" | ")
        winning = game[0].split(" ")
        hand = game[1].split(" ")
        count = 0
        while "" in winning:
            winning.remove("")
        for each in winning:
            if each in hand:
                if count == 0:
                    count = 1
                else:
                    count *= 2
        points += count
        point_map[i+1] = count

    return points

def part2(data):
    points = 0
    global point_map
    copies = {}
    for i in range(1, max(point_map.keys())+1):
        copies[i] = 1
    for k, v in point_map.items():
        card = k
        points = v
        for _ in range(copies[card]):
            temp_card = card
            temp_points = points
            while True:
                if temp_points < 1:
                    break
                else:
                    temp_card += 1
                    if temp_card not in point_map.keys():
                        break
                    temp_points /= 2
                    copies[temp_card] += 1
    return sum(copies.values())


file = "data/day4.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
