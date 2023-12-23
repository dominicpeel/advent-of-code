import sys
sys.setrecursionlimit(99999)
grid = [list(row) for row in open("inp23").read().strip().splitlines()]

S = (0,1)
E = (len(grid)-1,len(grid[0])-2)

p1 = 0

dirs = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}

def backtrack(i,j,steps=0):
    global p1
    if (i,j) == E:
        p1 = max(steps, p1)
        return 

    for di, dj in dirs.values():
        ni, nj = i+di, j+dj
        tile = grid[ni][nj] 
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if tile == ".":
                grid[ni][nj] = "O"
                backtrack(ni,nj,steps+1)
                grid[ni][nj] = "."
            elif tile in dirs:
                ddi, ddj = dirs[tile]
                nni, nnj = ni+ddi, nj+ddj
                if grid[nni][nnj] == ".":
                    grid[ni][nj] = "O"
                    grid[nni][nnj] = "O"
                    backtrack(nni,nnj,steps+2)
                    grid[ni][nj] = tile
                    grid[nni][nnj] = "."

# Part 1
backtrack(*S)
print(p1)

# Part 2
# long paths followed by choice dir
# convert to graph problem with weighted edges = len path to next dir change
# then dfs
grid = [list(row) for row in open("inp23").read().strip().splitlines()]

adj = {S:{}, E:{}}
for i, row in enumerate(grid):
    for j, tile in enumerate(row):
        if tile == "#": continue

        for di, dj in dirs.values():
            ni, nj = i+di, j+dj
            if grid[ni][nj] == ".":
                break
        else:
            adj[(i,j)] = {}

# dfs discovery of nodes
for i, j in adj:
    stack = [(i,j,0)]
    seen = {(i,j)}
    
    while stack:
        ii, jj, steps = stack.pop()
        
        if steps > 0 and (ii,jj) in adj:
            adj[(ii,jj)][(i,j)] = steps
            continue

        for di, dj in dirs.values():
            ni, nj = ii+di, jj+dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != "#" and (ni,nj) not in seen:
                stack.append((ni,nj,steps+1))
                seen.add((ni,nj))

# backtrack
p2 = 0
seen = {S}
def backtrack(i,j,steps=0):
    global p2
    if (i,j) == E:
        p2 = max(steps, p2)
        return 

    for n in adj[(i,j)]:
        if n not in seen:
            seen.add(n)
            backtrack(*n,steps+adj[(i,j)][n]) 
            seen.remove(n)

backtrack(*S)
print(p2)

