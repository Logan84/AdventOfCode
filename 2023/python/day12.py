# condition records of which springs are damager (the input) are also damaged
# help repair the damaged records

# springs are arranged into rows
#   for each row
#       if element is .: operational
#       if element is #: damaged
#       if element is ?: unknown
#   each row has contiguous group of damaged springs at the end
#   #### would be 4 not 2,2 or 1,3 
# goal: figure out how many different arrangements of operational and damaged can fit
# return the sum of all possible arangements
states = {}
def possible_arrangement(springs, numbers):
    if springs == "":
        return 1 if numbers == () else 0
    if numbers == ():
        return 1 if "#" not in springs else 0
    
    key = (springs, numbers)

    if key in states:
        return states[key]

    count = 0

    if springs[0] == '.' or springs[0] == '?':
        count += possible_arrangement(springs[1:], numbers)

    if springs[0] == '#' or springs[0] == '?':
        if numbers[0] <= len(springs):
            if "." not in springs[:numbers[0]]:
                if (numbers[0] == len(springs) or springs[numbers[0]] != "#"):
                    count += possible_arrangement(springs[numbers[0]+1:], numbers[1:])

    states[key] = count
        
    return count 

def part1(data):
    num_of_arangements = 0
    for line in data:
        spring, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        num_of_arangements += possible_arrangement(spring, nums)
    return num_of_arangements

def part2(data):
    num_of_arangements = 0
    for line in data:
        spring, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        nums *= 5
        spring = "?".join([spring]*5)
        num_of_arangements += possible_arrangement(spring, nums)
    return num_of_arangements

    return 0


file = "data/12.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
