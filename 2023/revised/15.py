from functools import reduce

seq = open("inp15").read().strip().split(",")

hash = lambda string: reduce(lambda curr, ch: (curr+ord(ch))*17%256, string, 0)

print(sum(map(hash, seq)))

boxes = [{} for _ in range(265)]
for string in seq:
    match string.strip("-").split("="):
        case [label, focal_len]: boxes[hash(label)][label] = int(focal_len)
        case [label]: boxes[hash(label)].pop(label, None)

print(sum(n*i*focal_len for n, box in enumerate(boxes, 1) for i, focal_len in enumerate(box.values(), 1)))

