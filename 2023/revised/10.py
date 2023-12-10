grid = {complex(i,j): col for i, row in enumerate(open("inp10")) for j, col in enumerate(row.strip())}

N, S, E, W = -1, 1, 1j, -1j
types = {
    "|": (N, S),
    "-": (E, W),
    "L": (N, E),
    "J": (N, W),
    "7": (S, W),
    "F": (S, E),
    "S": (N, E, S, W),
    ".": ()
}

graph = {pos: {pos+dir for dir in types[tile]} for pos, tile in grid.items()}
start = [pos for pos, tile in graph.items() if len(tile) == 4][0]

seen = {start}
while todo := graph[start]:
    curr = todo.pop()
    seen |= {curr}
    todo |= graph[curr]-seen

# Part 1
print(len(seen)//2)

# Part 2
p2 = 0
for pos in set(grid)-seen:
    hits = 0
    for i in range(int(pos.imag)):
        ipos = complex(pos.real, i)
        hits += grid[ipos] in "|JLS" and ipos in seen
    p2 += hits % 2

print(p2)

