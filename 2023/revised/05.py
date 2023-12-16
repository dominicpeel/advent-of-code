seeds, *maps = open("inp5").read().strip().split("\n\n")
seeds = [int(x) for x in seeds.split()[1:]]

mappings = []
for index, map in enumerate(maps):
    map = [x.split() for x in map.split("\n")[1:]]
    mappings.append({})
    for m in map:
        m = [int(x) for x in m]
        mappings[index][(m[1], m[1]+m[2])] = m[0]

p1 = seeds.copy()
for map in mappings:
    for i, curr in enumerate(p1):
        for l, r in map:
            if l <= curr < r:
                p1[i] = map[(l,r)] + curr-l
                break
print(min(p1))

seeds = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
for map in mappings:
    new_seeds = []
    i = 0
    while i < len(seeds):
        x, y = seeds[i]
        for l, r in map:
            if l <= x < r:
                if y <= r:
                    x = map[(l,r)] + x-l
                    y = map[(l,r)] + y-l
                    new_seeds.append((x,y))
                    break
                else: 
                    x = map[(l,r)] + x-l
                    ny = map[(l,r)] + r-l
                    new_seeds.append((x,ny))
                    seeds.append((r, y))
                    break
            if x < l and l < y < r:
                nx = map[(l,r)] + l-l
                y = map[(l,r)] + y-l
                new_seeds.append((nx,y))
                seeds.append((x, l))
                break
        else:
            new_seeds.append((x,y))
        i += 1
    seeds = new_seeds

print(min(seed[0] for seed in seeds))

