from collections import defaultdict, deque
grid = [list(line) for line in open("inp16").read().strip().split("\n")]
dirs = ((-1,0),(0,1),(1,0),(0,-1)) # NESW

def energize(row, col, dir):
    seen = defaultdict(set)

    res = 0
    q = deque([(row, col, dir)])
    while q:
        i, j, d = q.popleft()

        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])):
            continue

        if d in seen[(i,j)]:
            continue

        curr = grid[i][j]
        res += not seen[(i,j)]
        seen[(i,j)].add(d)

        match curr:
            case "." | "#":
                q.append((i+dirs[d][0], j+dirs[d][1], d))
            case "/":
                d = d+1 if d in [0,2] else d+3
                d %= 4
                q.append((i+dirs[d][0],j+dirs[d][1], d))
            case "\\":
                d = d+1 if d in [1,3] else d+3
                d %= 4
                q.append((i+dirs[d][0],j+dirs[d][1],d))
            case "|":
                if d in [1,3]:
                    q.append((i-1, j, 0))
                    q.append((i+1, j, 2))
                else:
                    q.append((i+dirs[d][0], j+dirs[d][1], d))
            case "-":
                if d in [0,2]:
                    q.append((i, j-1, 3))
                    q.append((i, j+1, 1))
                else:
                    q.append((i+dirs[d][0], j+dirs[d][1], d))
    return res

print(energize(0,0,1))

p2 = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if row == 0:
            p2 = max(p2, energize(row,col,2))
        elif row == len(grid):
            p2 = max(p2, energize(row,col,0))

        if col == 0:
            p2 = max(p2, energize(row,col,1))
        if col == len(grid[0]):
            p2 = max(p2, energize(row,col,3))

print(p2)

