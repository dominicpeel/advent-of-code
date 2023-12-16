grid = [list(row) for row in open("inp14").read().strip().split("\n")]

p1 = 0
for j in range(len(grid[0])):
    prev_stop = 0 
    for i in range(len(grid)):
        if grid[i][j] == "O":
            grid[i][j] = "."
            grid[prev_stop][j] = "O"
            p1 += len(grid) - prev_stop 
            prev_stop += 1
        elif grid[i][j] == "#":
            prev_stop = i+1

print(p1)
for row in grid:
    print("".join(row))

p2 = 0

grid = [list(row) for row in open("inp14").read().strip().split("\n")]
def cycles(N):
    seen = {}
    for cycle in range(N):
        # north
        for j in range(len(grid[0])):
            prev_stop = 0 
            for i in range(len(grid)):
                if grid[i][j] == "O":
                    grid[i][j] = "."
                    grid[prev_stop][j] = "O"
                    prev_stop += 1
                elif grid[i][j] == "#":
                    prev_stop = i+1

        # west
        for i in range(len(grid)):
            prev_stop = 0
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    grid[i][j] = "."
                    grid[i][prev_stop] = "O"
                    prev_stop += 1
                elif grid[i][j] == "#":
                    prev_stop = j+1

        # south
        for j in range(len(grid[0])):
            prev_stop = len(grid)-1
            for i in range(len(grid)-1,-1,-1):
                if grid[i][j] == "O":
                    grid[i][j] = "."
                    grid[prev_stop][j] = "O"
                    prev_stop -= 1
                elif grid[i][j] == "#":
                    prev_stop = i-1

        # east
        for i in range(len(grid)):
            prev_stop = len(grid[0])-1
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j] == "O":
                    grid[i][j] = "."
                    grid[i][prev_stop] = "O"
                    prev_stop -= 1
                elif grid[i][j] == "#":
                    prev_stop = j-1

        grid_copy = tuple((i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] =="O")
        if grid_copy in seen and N == 1_000_000_000:
            return cycle, seen[grid_copy]
        seen[grid_copy] = cycle

    return 0, 0

cycle_len, start = cycles(1_000_000_000)
remaining_cycles = start + ((1_000_000_000-start) % cycle_len)
print(remaining_cycles)
print(cycles(remaining_cycles))

# total load
p2 = 0
for i in range(len(grid)):
    for col in grid[i]:
        if col == "O":
            p2 += len(grid)-i
print(p2)

