from collections import defaultdict
lines = [line.strip() for line in open("inp4").readlines()]
newlines = 0
p1 = 0
bonus = defaultdict(lambda:1)
for i, line in enumerate(lines):
    winning, nums = line.split(": ")[1].split(" | ")
    winning = set([int(x) for x in winning.split(" ") if x])
    m = 0
    for num in [int(x) for x in nums.split(" ") if x]:
        if num in winning: 
            m += 1
    for j in range(i+1, i+1+(m)):
        bonus[j] += bonus[i] 
        newlines += bonus[i] 
    p1 += 2**(m-1) if m else 0

print(p1)
print(newlines + len(lines))

