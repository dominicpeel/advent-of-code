from collections import deque

grid = open("inp21").read().strip().split("\n")
graph = {i + j*1j: grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "."}

S = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "S":
            S = complex(i,j)
            graph[S] = "."

def flood(remaining_steps):
    q = deque([(S, remaining_steps)])
    seen = {S}
    seen_even = set()
    while q:
        curr, steps = q.popleft()

        if steps % 2 == 0:
            seen_even.add(curr)
        if steps == 0:
            continue

        for dir in (-1j, 1, 1j, -1):
            new = curr+dir
            if complex(new.real%len(grid), new.imag%len(grid[0])) in graph and new not in seen:
                seen.add(new)
                q.append((new, steps-1))

    return len(seen_even)
# Part 1
print(flood(64))

# Part 2
import numpy as np

points = [(m,flood(65+m*len(grid))) for m in range(3)]
p = np.polyfit(*zip(*points), 2)
print(round(np.polyval(p, 26501365//len(grid))))

