# Basically poker 
# five > four > full house > three > two pair > one pair > high
# Cards A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2
# if cards have same type, compare the first card in hand. Strong wins

# properly over engineered

class Hand():
    def __init__(self, hand, bid, part2 = False):
        self.hand = hand
        self.bid = int(bid)
        self.mapping = {"T":10, "J":11, "Q":12, "K":13, "A":14}
        self.part2 = part2 # handles for J meaning joker not jack
        if self.part2:
            self.mapping['J'] = 0
        self.strength = self.calculate_strength()
    def calculate_strength(self):
        temp = {}
        for each in self.hand:
            if each not in temp.keys():
                temp[each] = 1
            else:
                temp[each] += 1
        # updated jacks as jokers
        if self.part2:
            if 'J' in temp.keys():
                jokers = temp.pop('J')
                # 1 is not a joker or all are jokers five 5 of kind
                if(len(temp.keys()) == 1 or len(temp.keys()) == 0):
                    return 7
                # 2 are not jokers give 4 of kind or full house
                elif(len(temp.keys()) == 2):
                    if 3 in temp.values() or 1 in temp.values():
                        return 6
                    else:
                        return 5 # full house will have 2 cards with values 2 
                # 3 are not jokers give 3 of kind
                elif(len(temp.keys()) == 3):
                    return 4
                
                # 4 are not jokers give a pair
                elif(len(temp.keys()) == 4):
                    return 2
 
        # five of a kind
        if len(temp.keys()) == 1:
            return 7
        # high card
        elif len(temp.keys()) == 5: 
            return 1
        # one pair
        elif len(temp.keys()) == 4:
            return  2
        elif len(temp.keys()) == 3:
            if 3 in temp.values():
                # three of a kind
                return 4
            else:
                # two pair
               return  3
        elif len(temp.keys()) == 2:
            if 4 in temp.values():
                # four of a kind
               return  6
            else:
                # full house
               return 5
    def __lt__(self, value: object): # help with using a sorting algorithm
        if(self.strength < value.strength):
            return True
        elif (self.strength == value.strength):
            for ob1_card, ob2_card in zip(self.hand, value.hand):
                if ob1_card == ob2_card:
                    continue
                elif ob1_card.isdigit() and ob2_card.isdigit():
                    return int(ob1_card) < int(ob2_card)
                else:
                    if ob1_card in self.mapping.keys():
                        ob1_card = self.mapping[ob1_card]
                    if ob2_card in self.mapping.keys():
                        ob2_card = self.mapping[ob2_card]
                    return int(ob1_card) < int(ob2_card)

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
#            print("comparing {} and {}".format(arr[j+1].hand, arr[j].hand))
            if arr[j+1] < arr[j]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return

def part1(data):
    all_hands = []
    for line in data:
        hand, bid = line.strip("\n").split(" ")
        all_hands.append(Hand(hand, bid))
    bubbleSort(all_hands)
    multiplier = 1
    winnings = 0
    for i in range(0, len(all_hands)):
        winnings += (all_hands[i].bid * multiplier)
        multiplier += 1
    return winnings

def part2(data):
    all_hands = []
    for line in data:
        hand, bid = line.strip("\n").split(" ")
        all_hands.append(Hand(hand, bid, True)) # get all of the class representations of the hands
    bubbleSort(all_hands) # sort them to determine their strengths
    multiplier = 1
    winnings = 0
    for i in range(0, len(all_hands)): # add up all of the bids based on their strengths
        winnings += (all_hands[i].bid * multiplier)
        multiplier += 1
    for each in all_hands:
        print(each.hand, each.strength)
    return winnings


file = "data/day7.txt"
# Get the file read in 
with open(file, 'r') as f:
    data = f.readlines()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))
