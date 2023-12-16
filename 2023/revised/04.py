lines = open("inp4").readlines()
p1 = 0
cards = [1]*len(lines)
for i, line in enumerate(lines):
    winning, nums = line.split("|")
    winning = set(winning.split())
    nums = set(nums.split())
    m = len(winning & nums)
    for j in range(m):
        cards[i+1+j] += cards[i] 
    p1 += 2**(m-1) if m else 0

print(p1)
print(sum(cards))

