NORTH = [-1,0]
SOUTH = [1,0]
WEST = [0,-1]
EAST = [0,1]

maze = []
mapping = {"|":[NORTH, SOUTH],
           "-":[WEST, EAST], 
           "L":[NORTH, EAST],
           "J":[NORTH, WEST],
           "F":[SOUTH, EAST],
           "7":[WEST, SOUTH]
           }

def valid_north(northpoint):
    not_valid_values = ['L','-','J']
    if northpoint in not_valid_values:
        return False
    return True

def valid_south(southpoint):
    not_valid_values = ['F','-','7']
    if southpoint in not_valid_values:
        return False
    return True

def valid_west(westpoint):
    not_valid_values = ['J','|','7']
    if westpoint in not_valid_values:
        return False
    return True

def valid_east(eastpoint):
    not_valid_values = ['L','|','F']
    if eastpoint in not_valid_values:
        return False
    return True



def part1(data):
    global maze
    global mapping
    row_count = 0
    animal_location = None
    for line in data:
        row = [] 
        l = line.strip("\n")
        for char in l:
            if char == "S":
                row.append(0)
            else:
                row.append(char)
        maze.append(row)
        if 'S' in l:
            animal_location = [row_count, l.index('S')]
        row_count += 1
    for each in maze:
        print(each)
    points_to_process = []
    counter = 0
    while True:
        if counter == 0:
            n = [animal_location[0]+NORTH[0], animal_location[1]+NORTH[1]]
            s = [animal_location[0]+SOUTH[0], animal_location[1]+SOUTH[1]]
            e = [animal_location[0]+EAST[0], animal_location[1]+EAST[1]]
            w = [animal_location[0]+WEST[0], animal_location[1]+WEST[1]]
            if maze[n[0]][n[1]] in mapping.keys() and valid_north(maze[n[0]][n[1]]):
                print("valid north point: {}".format(maze[n[0]][n[1]])) 
                points_to_process.append(n)
            if maze[s[0]][s[1]] in mapping.keys():
                print("valid south point: {}".format(maze[s[0]][s[1]]))
                points_to_process.append(s)
            if maze[e[0]][e[1]] in mapping.keys():
                print("valid east point: {}".format(maze[e[0]][e[1]]))
                points_to_process.append(e)
            if maze[w[0]][w[1]] in mapping.keys(): 
                print("valid west point: {}".format(maze[w[0]][w[1]]))
                points_to_process.append(w)
            counter += 1
        elif len(points_to_process) == 0:
            break
        else:
            point = points_to_process.pop()
            print("Processing point: {}".format(maze[point[0]][point[1]]))

    print(maze)
    print("Animal at: {}, proof: {}".format(animal_location, maze[animal_location[0]][animal_location[1]]))

    return 0

def part2(data):
    return 0


file = "data/temp.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
