import math

instructions, nodes = open("inp8").read().strip().split("\n\n")
map = {}
for line in nodes.split("\n"):
    parent, children = line.split(" = ")
    map[parent] = children[1:-1].split(", ")

key = {"L":0, "R":1}

# Part 1
curr = "AAA"
steps = 0
while curr != "ZZZ":
    ins = instructions[steps%len(instructions)]
    curr = map[curr][key[ins]]
    steps += 1

print(steps)

# Part 2
currs = [k for k in map if k[-1] == "A"]
stepss = []
for curr in currs:
    steps = 0
    while curr[-1] != "Z":
        ins = instructions[steps%len(instructions)]
        curr = map[curr][key[ins]]
        steps += 1
    stepss.append(steps)

print(math.lcm(*stepss))

