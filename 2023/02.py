lines = [line.strip() for line in open("inp2").readlines()]
p1 = 0
p2 = 0
for i, line in enumerate(lines):
    isValid = True
    moves = line.split(": ")[1]
    iter = moves.split(";")
    rmin = gmin = bmin = 0
    for picks in iter:
        r, g, b = 12, 13, 14
        r2, g2, b2 = 0, 0, 0
        picks = picks.split(", ")
        for pick in picks:
            n, color = pick.strip().split(" ")
            n = int(n)
            if color == "red":
                r -= n
                r2 += n
                if r < 0:
                    isValid = False
            elif color == "green":
                g -= n
                g2 += n
                if g < 0:
                    isValid = False
            else:
                b -= n
                b2 += n
                if b < 0:
                    isValid = False
        rmin, gmin, bmin = max(r2, rmin), max(g2, gmin), max(b2, bmin)
    
    p2 += rmin*gmin*bmin
    if isValid:
        p1 += i+1

print(p1)
print(p2)
