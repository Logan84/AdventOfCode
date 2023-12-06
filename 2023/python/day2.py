def part1(data):
    RED = 12
    GREEN = 13
    BLUE = 14

    id_sums = 0
    id = 1
    for line in data:
        colon_index = line.find(":")
        games_list = line[colon_index+1:].strip('\n')
        games = games_list.split(';')
        status = 1
        for game in games:
            temp = game.split(" ")[1:]
            num = 0
            for each in temp:
                if each.isdigit():
                    num = int(each)
                else:
                    each = each.strip(',')
                    if each == 'blue' and num > BLUE:
                        status = 0
                    if each == 'green' and num > GREEN:
                        status = 0
                    if each == 'red' and num > RED:
                        status = 0
        if status != 0:
            id_sums += id
        id += 1 
    return id_sums

def part2(data):
    sum = 0 
    for line in data:
        red = 0
        blue = 0
        green = 0

        colon_index = line.find(":")
        games_list = line[colon_index+1:].strip('\n')
        games = games_list.split(';')
        for game in games:
            temp = game.split(" ")[1:]
            num = 0
            for each in temp:
                if each.isdigit():
                    num = int(each)
                else:
                    each = each.strip(',')

                    if each == 'blue':
                        blue = max(num, blue)
                    if each == 'green':
                        green = max(green, num)
                    if each == 'red':
                        red = max(red, num)
        sum += (red * green * blue)
    return sum



file = "data/day2.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print(part1(data))
    print(part2(data))
