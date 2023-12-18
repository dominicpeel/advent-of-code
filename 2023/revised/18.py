instructions = [line.split(" ") for line in open("inp18").read().strip().split("\n")]

dirs = {"R": 1j, "D": 1, "L": -1j, "U": -1}

def f(deltas):
    curr = perimeter = area = 0
    for d in deltas:
        curr += d
        area += curr.imag*d.real
        perimeter += abs(d.real+d.imag)

    return int(abs(area) + perimeter//2 +1)

# Part 1
print(f([dirs[dir]*int(steps) for dir, steps, _ in instructions]))

# Part 2
dirs = list(dirs.values())
print(f([dirs[int(hex[-2])] * int(hex[2:-2], 16) for _, _, hex in instructions]))

