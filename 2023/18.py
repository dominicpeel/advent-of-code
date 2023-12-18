from collections import deque

instructions = [line.split(" ") for line in open("inp18").read().strip().split("\n")]
dirs = {"R": 1j, "D": 1, "L": -1j, "U": -1}

curr = 0
dug = {curr}
p1 = 0

for dir, steps, _ in instructions:
    steps = int(steps)
    p1 += steps
    for step in range(steps):
        curr += dirs[dir]
        dug.add(curr)

q = deque([1+1j])
while q:
    curr = q.popleft()

    if curr in dug:
        continue
    dug.add(curr)

    p1 += 1

    for dir in dirs.values():
        q.append(curr+dir)

print(p1)

curr = 0
dirs = list(dirs.values())
vertices = [curr]

perimeter = 0
for _, _, hex in instructions:
    dir = int(hex[-2])
    steps = int(hex[2:-2], 16)

    perimeter += steps
    curr += steps*dirs[dir]
    vertices.append(curr)

area = 0
for a,b in zip(vertices, vertices[1:]):
    area += a.real*b.imag - a.imag*b.real

print(perimeter//2 + 1 + abs(area//2))

