maps = [lines for lines in open("inp5").read().strip().split("\n\n")]

seeds = [int(x) for x in maps[0].split()[1:]]
maps = maps[1:]
mappings = []
for index, map in enumerate(maps):
    map = [x.split() for x in map.split("\n")[1:]]
    mappings.append({})
    for m in map:
        m = [int(x) for x in m]
        # too slow/too much memory, use linear interpolation instead
        #for i in range(m[2]):
        #    mappings[index][m[1]+i] = m[0]+i
        mappings[index][(m[1], m[1]+m[2])] = m[0]

# p1 the lowest location number that corresponds to any of the initial seeds
p1 = seeds.copy()
for map in mappings:
    for i, curr in enumerate(p1):
        for l, r in map:
            if l <= curr < r:
                p1[i] = map[(l,r)] + curr-l
                break
print(min(p1))

# monotonically increasing so only need to worry about LB? Doesn't work cos right split might have a lower increment than left later on 
seeds = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]
for map in mappings:
    new_seeds = []
    i = 0
    while i < len(seeds):
        x, y = seeds[i]
        for l, r in map:
            # hope never recombining ranges causes problems
            # if l <= x,y < r , can apply range nicely
            if l <= x < r:
                if y <= r:
                    x = map[(l,r)] + x-l
                    y = map[(l,r)] + y-l
                    new_seeds.append((x,y))
                    break
                else: 
                    # if l <= x < r but y >= r, create new range for x then deal with y range later
                    x = map[(l,r)] + x-l
                    ny = map[(l,r)] + r-l
                    new_seeds.append((x,ny))
                    seeds.append((r, y))
                    break
            # if x < l, but y within range
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

