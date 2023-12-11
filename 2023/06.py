lines = [x.split()[1:] for x in open("inp6").readlines()]
races = []

for r in range(len(lines[0])):
    races.append([int(lines[0][r]), int(lines[1][r])])

p1 = 1
for time, distance in races:
    wins = 0
    for ms in range(time):
        if distance < ms*(time-ms):
            wins += 1
    p1 *= wins

print(p1)

time, distance = [int("".join(x.split()[1:])) for x in open("inp6").readlines()]
p2 = 0
for ms in range(time):
    if distance < ms*(time-ms):
        p2 += 1

print(p2)

