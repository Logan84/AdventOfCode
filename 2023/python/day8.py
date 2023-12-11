# input: left-right instructions 
# Starting point AAA, end point ZZZ
# Literally tree traversal but lets try with maps
from math import gcd
map = {}
instructions = None
def part1(data):
    global map
    global instructions

    data.remove("\n")
    for i, line in enumerate(data):
        if i == 0:
            instructions = line.strip("\n")
        else:
            location, steps = line.split(" = ")
            steps = steps.strip('(').strip('\n').strip(')').split(", ")
            map[location] = steps
    counter = 0
    instruction = 0
    state = 'AAA'
    while state != 'ZZZ':
        step = instructions[instruction]
        if step == 'R':
            state = map[state][1]
        else:
            state = map[state][0]
        counter += 1
        instruction += 1
        if instruction == len(instructions):
            instruction = 0

    return counter

def part2(data):
    global map
    global instructions
    starting_points = [x for x in map.keys() if x.endswith('A')]
    potential_end_points = [x for x in map.keys() if x.endswith('Z')]
    print(starting_points)
    print(potential_end_points)
    status = True
    count = 0
    instruction = 0

    p = starting_points[0]
    visited = [{},{},{},{},{},{}]
    loops = [0,0,0,0,0,0]
    while status:
        step = instructions[instruction]
        for i in range(len(starting_points)):
            if loops[i]:
                continue
            if step == 'R':
                starting_points[i] = map[starting_points[i]][1]
            else:
                starting_points[i] = map[starting_points[i]][0]
        for i in range(len(starting_points)):
            if loops[i]:
                continue
            if starting_points[i] in potential_end_points:
                print(starting_points[i], count)
                if starting_points[i] not in visited[i].keys():
                    visited[i][starting_points[i]] = count
                elif starting_points[i] in visited[i].keys():
                    print("loop found")
                    loops[i] += 1
        if 0 not in loops:
            break

        count += 1
        instruction += 1
        if instruction == len(instructions):
            instruction = 0
    numbers = []
    for each in visited:
        for k in each.keys():
            numbers.append(each[k])
    print(numbers)
    LCM = numbers.pop()
    for num in numbers:
        LCM = LCM * num // gcd(LCM, num)
    print(LCM)
    return LCM


file = "data/day8.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
