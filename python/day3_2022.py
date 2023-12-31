# Day 3: Rucksack Reorganization
# part 1

# rucksacks have 2 compartments
#     given types go into one of two compartments

# EXAMPLE
# input = "vJrwpWtwJgWrhcsFMMfFFhFp"
# first_half = "vJrwpWtwJgWr"
# second_half = "hcsFMMfFFhFp"
# similarity = "p"
# every item can be converted to a priority, i.e. a-z == 1-26, A-Z == 27-52
# find the sum of the priorities of the item types
letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = letters.upper()
count = 1
priority = {}
for i in( letters + upper_letters ):
    priority[i] = count
    count += 1

# Input

items_in_rucksack = open("inputs/day3_input.txt", 'r')
items_in_rucksack = items_in_rucksack.readlines()
#
# items_in_rucksack = ["JrwpWtwJgWrhcsFMMfFFhFp",
# "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
# "PmmdzqPrVvPwwTWBwg",
# "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
# "ttgJtRGJQctTZtZT",
# "CrZsJsPPZsGzwwsLwLmpwMDw"]
#

sum = 0
# Loop through each item
for each in items_in_rucksack:
    # split the string in half
    first_half = each[0:int(len(each)/2)]
    second_half = each[int(len(each)/2):]
    for letter in first_half:
        if letter in second_half:
            sum += priority[letter]
            break

print(sum)

# Part 2
sum = 0
bag_of_three = []
for each in items_in_rucksack:
    bag_of_three.append(each)
    if(len(bag_of_three)) != 3:
        continue
    for letter in bag_of_three[0]:
        if letter in bag_of_three[1] and letter in bag_of_three[2]:
            sum += priority[letter]
            break
    bag_of_three = []

print(sum)

