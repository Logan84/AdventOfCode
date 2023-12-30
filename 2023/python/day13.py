def reflection_with_smudge(landscape, reflection_row):
    a1 = landscape[:reflection_row]
    a2 = landscape[reflection_row:]
    distance_to_check = min(len(a1), len(a2))
    temp1 = a1[::-1][:distance_to_check]
    temp2 = a2[:distance_to_check]

    mismatch = 0
    for line1, line2 in zip(temp1, temp2):
        for char1, char2 in zip(line1, line2):
            if char1 != char2:
                mismatch += 1

    if mismatch == 1:
        return True

    return False


def reflection(landscape, reflection_row):
    a1 = landscape[:reflection_row]
    a2 = landscape[reflection_row:]
    distance_to_check = min(len(a1), len(a2))
    temp1 = a1[::-1][:distance_to_check]
    temp2 = a2[:distance_to_check]

    if temp1 == temp2:
        return True
    else:
        return False

def part1(data):
    problems = []
    temp = []
    total = 0
    data.append("\n")
    ref = False
    for line in data:
        if line != "\n":
            temp.append(line.strip("\n"))
        else:
            problems.append(temp)
            temp = []
    for problem in problems:
        #print("CHECKING ROW REFLECTION")
        for i in range(1, len(problem)):
            ref = reflection(problem, i)
            if ref:
                total += (100 * i)
                break
        temp = list(zip(*problem))
        #print("CHEKCING COLUMN REFLECTION")
        for i in range(1, len(temp)):
            ref = reflection(temp, i)
            if ref:
                total += i
                break
    return total

def part2(data):
    problems = []
    temp = []
    total = 0
    data.append("\n")
    ref = False
    for line in data:
        if line != "\n":
            temp.append(line.strip("\n"))
        else:
            problems.append(temp)
            temp = []
    for problem in problems:
        for i in range(1, len(problem)):
            ref = reflection_with_smudge(problem, i)
            if ref:
                total += (100 * i)
                break
        temp = list(zip(*problem))
        #print("CHEKCING COLUMN REFLECTION")
        for i in range(1, len(temp)):
            ref = reflection_with_smudge(temp, i)
            if ref:
                total += i
                break
    return total

file = "data/13.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
