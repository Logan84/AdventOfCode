def part1(data):
    time_array = []
    distance_array = []

    for i, line in enumerate(data):
        temp = line[line.find(":")+2:].strip("\n").split()
        while "" in temp:
            temp = temp.remove("")
        for each in temp:
            if i == 0:
                time_array.append(int(each))
            else:
                distance_array.append(int(each))
    counter = 0
    final_array = [0]*len(time_array)
    for time, dist in zip(time_array, distance_array):
        for t in range(time):
            charge_time = t
            run_time = time - t
            distance_travel = run_time * charge_time
            if distance_travel > dist:
                final_array[counter] += 1
        counter += 1
    print(final_array) 
    ans = 1
    for each in final_array:
        ans *= each
    return ans


def part2(data):
    time = ""
    distance = ""
    ans = 0
    for i, line in enumerate(data):
        temp = line[line.find(":")+2:].strip("\n").split()
        while "" in temp:
            temp = temp.remove("")
        for each in temp:
            if i == 0:
                time += each
            else:
                distance += each
    time = int(time)
    distance = int(distance)
    for t in range(time):
        charge_time = t
        run_time = time - t
        distance_travel = run_time * charge_time
        if distance_travel > distance:
            ans += 1
    return ans



file = "data/day6.txt"
# Get the file read in 
with open(file, 'r') as f:
    # starting speed is zerom/s
    # for each millisecond you spend holding dow the button, the boar speed increases by 1m/s
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
