# Part 1
# input is calories on each elf
file_of_calories = "inputs/day1_input.txt"
calories = open(file_of_calories, 'r')
lines = calories.readlines()

# begin gathering total calories
elves_holdings = []
elf_calories = 0
for line in lines:
    if line == '\n':
        elves_holdings.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(line)

elves_holdings.sort(reverse=True)
# Print out the highest
print(elves_holdings[0])

# Part 2
# Print out the three highest and sum them
print(elves_holdings[0:3])
print(sum(elves_holdings[0:3]))
