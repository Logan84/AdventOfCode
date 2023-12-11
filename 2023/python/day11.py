universe = []

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def create_universe(data):
    global universe
    for line in data:
        universe.append([x for x in line.strip("\n")])

def part1(scale):
    global universe
    total = 0
    # gather the locations of the universes
    galaxies = [(r, c) for r in range(len(universe)) for c in range(len(universe[r])) if universe[r][c] == "#"]
    paths = []

    # get the rows that do not contain galaxies
    rows_without_galaxies = [x for x in range(len(universe)) if "#" not in universe[x]]

    # get the columns that do not contain galaxies
    columns_without_galaxies = []
    c = 0
    for column in zip(*universe):
        if "#" not in column:
            columns_without_galaxies.append(c) 
        c += 1

    # create the paths that we need to calculate
    for i in range(len(galaxies)):
        for j in galaxies[i+1:]:
            paths.append([galaxies[i], j])

    # loop throught the paths and gather their distances
    # using manhattan distance which is |x1 - x2| + |y1 - y2|
    for p1, p2 in paths:
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])):
            # if going through a row without a galaxy, add the scale
            if x in rows_without_galaxies:
                total += scale
            else:
                total += 1 
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])):
            # if going through a column without a galaxy, add the scale
            if y in columns_without_galaxies:
                total += scale
            else:
                total += 1
        
    return total


file = "data/day11.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    create_universe(data)
    print("Part 1: {}".format(part1(scale = 2)))
    print("Part 2: {}".format(part1(scale = 1000000)))
