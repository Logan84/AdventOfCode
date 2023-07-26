#### Import libraries


#### input is calories on each elf
file_of_calories = "inputs/day1_input.txt"
calories = open(file_of_calories, 'r')
lines = calories.readlines()

#### begin gathering total calories
elves_holdings = []
elf_calories = 0
for line in lines:
    
    if line == '\n':
        elves_holdings.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(line)

#### Print out the highest
print(max(elves_holdings))