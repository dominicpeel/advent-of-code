lines = [list(map(int, line.strip().split(" "))) for line in open("inp9").readlines()]

p1 = p2 = 0
for line in lines:
    diffs = [line]
    while not all(d == 0 for d in diffs[-1]):
        diffs.append([b-a for a,b in zip(diffs[-1][:-1], diffs[-1][1:])])

    p1 += sum(diff[-1] for diff in diffs)
    p2 += sum(((-1)**(i%2))*diff[0] for i, diff in enumerate(diffs))

print(p1)
print(p2)

