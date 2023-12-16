import math

lines = [x.split()[1:] for x in open("inp6").readlines()]
races = [(int(lines[0][r]), int(lines[1][r])) for r in range(len(lines[0]))]

p1 = 1
for time, distance in races:
    d = math.sqrt(time**2 - 4*distance)
    a, b = .5*(time+d), .5*(time-d)
    if a > b: a, b = b, a
    p1 *= math.ceil(b-1)-math.floor(a+1)+1

print(p1)

time, distance = [int("".join(x.split()[1:])) for x in open("inp6").readlines()]
d = math.sqrt(time**2 - 4*distance)
a, b = .5*(time+d), .5*(time-d)
if a > b: a, b = b, a
p2 = math.ceil(b-1)-math.floor(a+1)+1

print(p2)

