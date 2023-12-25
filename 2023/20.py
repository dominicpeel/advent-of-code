import math
from collections import defaultdict, deque

lines = [line.split(" -> ") for line in open("inp20").read().strip().split("\n")]

modules = {}
for module, nodes in lines:
    nodes = nodes.split(", ")
    modules[module[1:]] = [module[0], nodes]

def configure():
    conj = defaultdict(dict)
    flip = {}
    for name, (module_type, nodes) in modules.items():
        for node in nodes:
            if node in modules and modules[node][0] == "&":
                conj[node][name] = "lo"
        if module_type == "%":
            flip[name] = False
    return conj, flip

conj, flip = configure()
lo = hi = 0
for i in range(1000):
    lo += 1
    q = deque([("roadcaster", node, "lo") for node in modules["roadcaster"][1]])
    while q:
        prev, curr, sig = q.popleft()

        if sig == "lo":
            lo += 1
        else:
            hi += 1

        if curr not in modules:
            continue

        module_type, nodes = modules[curr]
        if module_type == "%":
            if sig == "lo":
                flip[curr] = not flip[curr]
                for node in nodes:
                    q.append((curr, node, "hi" if flip[curr] else "lo"))
        else:
            conj[curr][prev] = sig
            for node in nodes:
                q.append((curr, node, "lo" if all(x == "hi" for x in conj[curr].values()) else "hi"))

# Part 1
print(lo*hi)

# Part 2
# conj going into rx so find first time each going into conj =1 and calc lcm
conj, flip = configure()
feed = next(module for module, (_, nodes) in modules.items() if "rx" in nodes)
seen = {prev: 0 for prev in conj[feed]}
pushes = 0
while True:
    pushes += 1
    q = deque([("roadcaster", node, "lo") for node in modules["roadcaster"][1]])
    while q:
        prev, curr, sig = q.popleft()

        if sig == "lo":
            lo += 1
        else:
            hi += 1

        if curr not in modules:
            continue

        module_type, nodes = modules[curr]
        if module_type == "%":
            if sig == "lo":
                flip[curr] = not flip[curr]
                for node in nodes:
                    q.append((curr, node, "hi" if flip[curr] else "lo"))
        else:
            conj[curr][prev] = sig
            for node in nodes:
                q.append((curr, node, "lo" if all(x == "hi" for x in conj[curr].values()) else "hi"))
                if node == "rx" and sig == "hi":
                    seen[prev] = pushes
                    if all(seen.values()):
                        print(math.lcm(*list(seen.values())))
                        exit()

