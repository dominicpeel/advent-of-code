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

manhattan = lambda a,b : abs(a[0]-b[0])+abs(a[1]-b[1])

galaxies = list(galaxies)
p1 = p2 = 0
for a in range(len(galaxies)):
    ai, aj = galaxies[a]
    for b in range(a+1, len(galaxies)):
        bi, bj = galaxies[b]

        row_expansions = sum(row in clear_rows for row in range(*sorted((ai, bi))))
        col_expansions = sum(col in clear_cols for col in range(*sorted((aj, bj))))

        p1 += row_expansions + col_expansions + manhattan(galaxies[a], galaxies[b])
        p2 += (1000000-1)*(row_expansions + col_expansions) + manhattan(galaxies[a], galaxies[b])

print(p1)
print(p2)

