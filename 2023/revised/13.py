patterns = [[list(row) for row in x.split("\n")] for x in open("inp13").read().strip().split("\n\n")]

def check(grid, exp_err): 

    for i in range(len(grid)-1):
        err = 0
        finished = False
        l, r = i, i+1
        while l >= 0 and r < len(grid):
            for col in range(len(grid[0])):
                if grid[l][col] != grid[r][col]:
                    if err > exp_err:
                        finished = True
                        break
                    err += 1
            if finished: break
            l -= 1
            r += 1
        else:
            if err == exp_err:
                return 100*(i+1)

    for i in range(len(grid[0])-1):
        err = 0
        l, r = i, i+1
        while l >= 0 and r < len(grid[0]):
            for row in range(len(grid)):
                if grid[row][l] != grid[row][r]:
                    if err == exp_err:
                        break
                    err += 1
            else:
                l -= 1
                r += 1
                continue
            break
        else:
            if err == exp_err:
                return i+1

    return 0

# Part 1
print(sum(check(grid, 0) for grid in patterns))
# Part 2
print(sum(check(grid, 1) for grid in patterns))

