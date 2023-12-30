def part1(data):
    total = 0
    tilted_platform = []
    for each in data:
        tilted_platform.append([x for x in each if x != "\n"])
    tilted_platform = list(zip(*tilted_platform))
    for each in tilted_platform:
        cube_rocks = [i for i, x in enumerate(each) if x == "#"]
        rolling_rocks = [i for i, x in enumerate(each) if x == "O"]

        new_column = []
        for i in range(len(each)):
            if rolling_rocks == [] and cube_rocks == []:
                new_column.append(",")

            if i == cube_rocks[0]:
                new_column.append("#")
                cube_rocks.pop()
            
            if rolling_rocks[0] < cube_rocks[0]:
                new_column.append("O")
                rolling_rocks.pop()

            else:
                new_column.append(",")
        

    return total

def part2(data):
    total = 0
    return total

file = "data/temp.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
