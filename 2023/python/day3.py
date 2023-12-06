def get_positions(point, max_x, max_y):
    positions_to_check = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
    positions = []
    for each in positions_to_check:
        temp = [point[0]+each[0], point[1]+each[1]]
        if temp[0] < 0:
            temp[0] = 0
        if temp[1] < 0:
            temp[1] = 0
        if temp[0] > max_x:
            temp[0] = max_x
        if temp[1] > max_y:
            temp[1] = max_y
        positions.append(temp)
    return positions

   
def part1(data):
    sum = 0
    position_of_symbols = []
    check_positions = []
    unique_position = []
    symbols = ['*','#','$','+']

    for i in range(len(data)):
        for j in range(len(data[0])):
            char = data[i][j]
            if char in symbols:
                position_of_symbols.append([i,j])

    for each in position_of_symbols:
        temp = get_positions(each, len(data), len(data[0]))
        for each in temp:
            if each not in check_positions:
                check_positions.append(each)
    for point in check_positions:
        x = point[0]
        y = point[1]
        if data[x][y].isdigit():
            datapoints = []
            datapoints.append([x, y])
            num = data[x][y]
            checkleft = True
            checkright = True
            temp = y
            while checkleft:
                temp -= 1
                if temp < 0:
                    checkleft = False
                elif data[x][temp].isdigit():
                    num = data[x][temp]+ num
                    print("in the elif")
                    datapoints.insert(0, [x,temp])
                else:
                    checkleft = False
            temp = y
            while checkright:
                temp += 1
                if temp > len(data[0]):
                    checkright = False
                elif data[x][temp].isdigit():
                    num = num + data[x][temp]
                    datapoints.append([x,y])
                    print("in the elif")
                else:
                    checkright = False
            if datapoints not in unique_position:
                unique_position.append(datapoints)
    print(unique_position)
    return sum
def part2(data):
    return 

file = "data/day3.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part1: {}".format(part1(data)))
