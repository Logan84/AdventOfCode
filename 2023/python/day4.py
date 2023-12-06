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

    print(point_map)
    return points

def part2(data):
    points = 0
    global point_map
    for k, v in point_map.items():
        print(k)
        print(v)
    return 0


file = "data/temp.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
