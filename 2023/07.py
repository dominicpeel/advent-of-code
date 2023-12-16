from collections import Counter
from functools import cmp_to_key, lru_cache
hands = [x.split() for x in open("inp7").readlines()]
strength = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")[::-1]

def cage_fight(a, b):
    for a, b in zip(a,b):
        if strength.index(a) > strength.index(b):
            return 1
        elif strength.index(a) < strength.index(b):
            return -1

def get_type(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 7 # 5 of kind
    if len(counts) == 2:
        max_count = max(c for c in counts.values())
        if max_count == 4:
            return 6 # 4 kind
        return 5 # full house
    if len(counts) == 3:
        max_count = max(c for c in counts.values())
        if max_count == 3:
            return 4 # three kind
        return 3 # two pair
    if len(counts) == 4:
        return 2 # one pair
    return 1 # high card

hands = [(hand, bid, get_type(hand)) for hand, bid in hands]

def compare(a, b):
    if a[2] > b[2]:
        return 1
    elif a[2] <  b[2]:
        return -1
    return cage_fight(a[0], b[0])

sorted_hands = sorted(hands, key=cmp_to_key(compare))
p1 = sum((i+1)*int(bid) for i, (_, bid, _) in enumerate(sorted_hands)) 
print(p1)

strength = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")[::-1]

@lru_cache
def get_type2(hand):
    counts = Counter(hand)
    if "J" not in counts:
        return get_type(hand)

    hand_arr = [*hand]
    max_type = get_type(hand)
    j_index = hand.find("J")
    for card in set(counts):
        if card == "J":
            continue
        hand_arr[j_index] = card
        max_type = max(max_type, get_type2("".join(hand_arr)))
        hand_arr[j_index] = "J"
    return max_type

hands = [(hand, bid, get_type2(hand)) for hand, bid, _ in hands]

sorted_hands = sorted(hands, key=cmp_to_key(compare))
p2 = sum((i+1)*int(bid) for i, (_, bid, _) in enumerate(sorted_hands)) 
print(p2)

