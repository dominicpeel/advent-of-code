patterns = [[list(row) for row in x.split("\n")] for x in open("inp13").read().strip().split("\n\n")]

def check(grid, prev=0): 
    for i in range(len(grid)-1):
        l, r = i, i+1
        while l >= 0 and r < len(grid):
            if grid[l] != grid[r]:
                break
            l -= 1
            r += 1
        else:
            if prev != 100*(i+1):
                return 100*(i+1)

    for i in range(len(grid[0])-1):
        l, r = i, i+1
        while l >= 0 and r < len(grid[0]):
            for row in range(len(grid)):
                if grid[row][l] != grid[row][r]:
                    break
            else:
                l -= 1
                r += 1
                continue
            break
        else:
            if prev != i+1:
                return i+1

    return 0

# Part 1
print(sum(check(grid) for grid in patterns))

p2 = 0
for grid in patterns:
    prev = check(grid)

    found = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curr = grid[i][j]
            grid[i][j] = "." if curr == "#" else "#"
            res = check(grid, prev)
            grid[i][j] = curr
            if res:
                p2 += res
                found = True
                break
        if found: break

# Part 2
print(p2)

