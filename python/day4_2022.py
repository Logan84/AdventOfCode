# Day 4: camp cleanup

def MakeListsFromString(string):
    string = string.split(',')
    a = string[0].split('-')
    b = string[1].split('-')
    a_range = [x for x in range(int(a[0]), int(a[1])+1)]
    b_range = [x for x in range(int(b[0]), int(b[1])+1)]
    return a_range, b_range


def SortListsBySize(list1, list2):
    if(len(list1) > len(list2)):
        return list2, list1
    return list1, list2


def CheckForListInList(list1, list2):
    ListinList = True
    for each in list1:
        if each not in list2:
            ListinList = False
    return ListinList


def CheckForAnyListOverlap(list1, list2):
    overlap = False
    for each in list1:
        if each in list2:
            overlap = True
    return overlap


examples = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]

file = "inputs/day4_input.txt"
pairs = open(file, 'r').readlines()
sum = 0
for example in pairs:
    a, b = MakeListsFromString(example)
    smaller, larger = SortListsBySize(a, b)
    list_in_list_check = CheckForListInList(smaller, larger)
    if(list_in_list_check):
        sum += 1

print(sum)


sum = 0
for example in pairs:
    a, b = MakeListsFromString(example)
    smaller, larger = SortListsBySize(a, b)
    list_overlap_check = CheckForAnyListOverlap(smaller, larger)
    if(list_overlap_check):
        sum += 1

print(sum)
