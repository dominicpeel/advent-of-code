import heapq
from collections import defaultdict
from math import inf

grid = [list(map(int, row)) for row in open("inp17").read().strip().split("\n")]
map = {complex(i,j): int(loss) for i, row in enumerate(grid) for j, loss in enumerate(row)}
end = complex(len(grid)-1, len(grid[0])-1)

def min_loss(min_steps, max_steps):
    heap = [(0,(0,0),(-1,0)), (0,(0,0),(0,-1))]
    seen = set()
    losses = defaultdict(lambda: inf)
    while heap:
        loss, pos, dir = heapq.heappop(heap)
        pos = complex(*pos)
        dir = complex(*dir)

        if pos == end:
            return loss

        if (pos, dir) in seen:
            continue
        seen.add((pos,dir))

        for rot in (-1j, 1j):
            new_dir = dir*rot
            path_loss = loss
            for dis in range(1, max_steps+1):
                new_pos = pos + dis*new_dir
                if new_pos in map:
                    path_loss += map[new_pos]
                    if dis < min_steps: continue
                    if path_loss < losses[(new_pos, new_dir)]:
                        losses[(new_pos, new_dir)] = path_loss
                        heapq.heappush(heap, (path_loss, (new_pos.real, new_pos.imag), (new_dir.real, new_dir.imag)))

print(min_loss(1,3))
print(min_loss(4,10))

