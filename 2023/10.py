from collections import deque

grid = [list(row.strip()) for row in open("inp10").read().replace("7", "$").split("\n")]

dirs = {"N": (-1,0), "S": (1,0), "E": (0,1), "W": (0,-1)}
types = {
"|": (dirs["N"], dirs["S"]),
"-": (dirs["E"], dirs["W"]),
"L": (dirs["N"], dirs["E"]),
"J": (dirs["N"], dirs["W"]),
"$": (dirs["S"], dirs["W"]),
"F": (dirs["S"], dirs["E"]),
"S": (dirs["N"], dirs["E"], dirs["S"], dirs["W"])
}

S = (0,0)
found = False
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "S":
            S = (i,j)
            found = True
            break
    if found: break

q = deque([(*S, 0)])
steps = 0
p1 = -1
while q:
    i, j, steps = q.popleft()
    p1 = max(p1, steps)
    if grid[i][j].isdigit():
        continue

    pipe = grid[i][j]
    grid[i][j] = str(steps)

    for di, dj in types[pipe]:
        ni, nj = i+di, j+dj
        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            continue
        if grid[ni][nj] not in types:
            continue

        if (-di,-dj) in types[grid[ni][nj]]:
            q.append((ni,nj,steps+1))

# Part 1
print(p1)

# Part 2
# Pre-process grid
grid_b = [list(row.strip()) for row in open("inp10").read().replace("7", "$").split("\n")]
new_grid = [["." for _ in range(len(grid[0])*3)] for _ in range(len(grid)*3)]
for i, row in enumerate(grid_b):
    for j, pipe in enumerate(row):
        if grid[i][j].isdigit():
            new = [["." for _ in range(3)] for _ in range(3)]
            new[1][1] = "#"
            mid = (1,1)
            for dir in dirs.values():
                if dir in types[pipe]:
                    new[1+dir[0]][1+dir[1]] = "#"
            for ni in range(3):
                for nj in range(3):
                    new_grid[(i*3)+ni][(j*3)+nj] = new[ni][nj]


# flood spaces to create disjoint sets
# then see which sets hit the edge
flood = deque([(0,0)])
while flood:
    i, j = flood.popleft()
    if new_grid[i][j] != ".":
        continue
    new_grid[i][j] = "0"
    for ni in range(i-1,i+2):
        for nj in range(j-1,j+2):
            if 0 <= ni < len(new_grid) and 0 <= nj < len(new_grid[0]):
                flood.append((ni,nj))

p2 = 0
for i, row in enumerate(grid_b):
    for j, tile in enumerate(row):
        if new_grid[i*3+1][j*3+1] == ".":
            new_grid[i*3+1][j*3+1] = "@"
            p2 += 1

print(p2)

