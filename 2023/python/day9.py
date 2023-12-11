lists_of_lists = []
def part1(data):
    global lists_of_lists
    sum = 0
    for line in data:
        series = list(map(int, line.strip("\n").split(" ")))
        lists_of_lists = [series]
        temp = []
        while list(set(temp)) != [0]:
            temp = []
            curr_list = lists_of_lists[-1]
            for i in range(len(curr_list)-1):
                temp.append(curr_list[i+1] - curr_list[i])
            lists_of_lists.append(temp)
        for i in range(len(lists_of_lists)-1 ,-1, -1):
            curr_list = lists_of_lists[i]
            if i == len(lists_of_lists)-1:
                curr_list.append(0)
            else:
                curr_list.append(curr_list[-1] + lists_of_lists[i+1][-1])
        #print(lists_of_lists)
        sum += lists_of_lists[0][-1]
    print(lists_of_lists)
    return sum

def part2(data):
    global lists_of_lists
    sum = 0
    for line in data:
        series = list(map(int, line.strip("\n").split(" ")))
        lists_of_lists = [series]
        temp = []
        while list(set(temp)) != [0]:
            temp = []
            curr_list = lists_of_lists[-1]
            for i in range(len(curr_list)-1):
                temp.append(curr_list[i+1] - curr_list[i])
            lists_of_lists.append(temp)

        for i in range(len(lists_of_lists)-1, -1, -1):
            curr_list = lists_of_lists[i]
            if i == len(lists_of_lists)-1:
                curr_list.insert(0, 0)
            else:
                curr_list.insert(0, curr_list[0] - lists_of_lists[i+1][0])
            
        #print(lists_of_lists)
        sum += lists_of_lists[0][0]

    return sum
file = "data/day9.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
