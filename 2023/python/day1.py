def part1(data):
    nums = []
    for line in data:
        digits = []
        for i in line:
            if i.isdigit():
                digits.append(int(i))
        nums.append(digits[0]*10 + digits[-1])
    return sum(nums)

def part2(data):
    new_data = []
    mappings = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
                'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for line in data:
        final_string = ''
        string = ''
        temp = line.strip()
        for char in temp:
            digit = None
            if char.isdigit():
                digit = char
            else:
                string += char
                for key, value in mappings.items():
                    if string.endswith(key):
                        digit = str(value)
            if digit is not None:
                final_string += str(digit)
        new_data.append(final_string)
    return new_data


file = "data/day1.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    new_data = part2(data)
    print("Part 2: {}".format(part1(new_data)))
