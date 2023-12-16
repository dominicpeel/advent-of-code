seq = open("inp15").read().strip()

def hash(string):
    curr = 0
    for ch in string:
        curr = (17*(curr+ord(ch)))%256
    return curr

print(sum(hash(string) for string in seq.split(",")))

boxes = [{} for _ in range(265)]
for string in seq.split(","):
    if string[-1] == "-":
        label = string[:-1]
        boxes[hash(label)].pop(label, None)
    else:
        label, focal_len = string.split("=")
        boxes[hash(label)][label] = int(focal_len)

p2 = 0
for n, box in enumerate(boxes):
    for i, focal_len in enumerate(box.values()):
        p2 += (n+1)*(i+1)*focal_len

print(p2)

