grid = [list(row.strip()) for row in open("inp11").read().strip().split("\n")]

clear_rows = {*range(len(grid))}
clear_cols = {*range(len(grid[0]))}
galaxies = set()

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "#":
            clear_rows.discard(i)
            clear_cols.discard(j)
            galaxies.add((i,j))

c = 0
row_expansions = [c := (c+1) if row in clear_rows else c for row in range(len(grid))]
c = 0
col_expansions = [c := (c+1) if col in clear_cols else c for col in range(len(grid[0]))]

manhattan = lambda a,b : abs(a[0]-b[0])+abs(a[1]-b[1])

galaxies = list(galaxies)
p1 = p2 = 0
for a in range(len(galaxies)):
    ai, aj = galaxies[a]
    for b in range(a+1, len(galaxies)):
        bi, bj = galaxies[b]

        p1 += abs(row_expansions[bi] - row_expansions[ai]) + abs(col_expansions[bj]-col_expansions[aj]) + manhattan(galaxies[a], galaxies[b])
        p2 += (1000000-1) * (abs(row_expansions[bi] - row_expansions[ai]) + abs(col_expansions[bj]-col_expansions[aj])) + manhattan(galaxies[a], galaxies[b])

print(p1)
print(p2)

