from collections import defaultdict

grid = [list(line.strip()) for line in open("inp3").readlines()]

def check_adj(i, j):
    for di in range(max(0, i-1), min(len(grid), i+2)):
        for dj in range(max(0, j-1), min(len(grid[0]), j+2)):
            item = grid[di][dj]
            if not (item.isdigit() or item == "."):
                return False
    return True

p1 = 0
for i, row in enumerate(grid):
    curr = 0
    failed = False
    for j, ch in enumerate(row):
        if ch.isdigit():
            curr = 10*curr + int(ch)
            if not check_adj(i, j):
                failed = True
        else:
            if failed and curr > 0:
                p1 += curr
            curr = 0
            failed = False 
    if failed:
        p1 += curr

print(p1)

# bfs on gears
def discover_num(i, j):
    l = r = j
    while l >= 0 and grid[i][l].isdigit():
        l -= 1
    while r < len(grid[0]) and grid[i][r].isdigit():
        r += 1
    return l, int("".join(grid[i][l+1:r]))

def find_adj(i, j):
    bounds = set() #(row, start) []
    res = []
    for di in range(max(0, i-1), min(len(grid), i+2)):
        for dj in range(max(0, j-1), min(len(grid[0]), j+2)):
            item = grid[di][dj]
            if item.isdigit():
                l, num = discover_num(di,dj)
                if (di, l) not in bounds:
                    bounds.add((di,l))
                    res.append(num)
    if len(res) == 2:
        return res[0]*res[1]
    return 0


p2 = 0
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        if ch == "*":
            p2 += find_adj(i,j)
print(p2)

