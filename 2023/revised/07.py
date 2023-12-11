import math
from collections import Counter

data = open("inp7").read().strip()
strength = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2, *".split(", ")[::-1]

def get_type(hand):
    counts = Counter(hand)
    jokers = counts["*"]
    if jokers < 5:
        max_card = max(counts, key=counts.get)
        counts[max_card] += jokers

    entropy = 0
    for card in set(hand):
        if card == "*": continue
        p = counts[max_card] / len(hand)
        entropy -= p*math.log(p)

    return -entropy # lower entropy = higher rank

def total(data):
    hands = [line.split() for line in data.split("\n")]
    sorted_hands = sorted((get_type(hand), *map(strength.index, hand), bid) for hand, bid in hands)
    return sum(rank*int(bid) for rank, (*_, bid) in enumerate(sorted_hands, 1)) 

# Part 1
print(total(data))

# Part 2
data = data.replace("J", "*")
print(total(data))

