hailstones = [[list(map(int, vector.split(", "))) for vector in line.split(" @ ")] for line in open("inp24").read().strip().split("\n")]

bnd = [200000000000000, 400000000000000]
#bnd = [7, 27]

p1 = 0
for i in range(len(hailstones)):
    for j in range(i+1, len(hailstones)):
        a_pos, a_vel = hailstones[i]
        b_pos, b_vel = hailstones[j]

        a_px, a_py, a_pz = a_pos
        b_px, b_py, b_pz = b_pos

        a_vx, a_vy, a_vz = a_vel
        b_vx, b_vy, b_vz = b_vel


        if b_vx * a_vy == b_vy * a_vx:
            continue
        
        ta = ((b_py - a_py) * b_vx - (b_px - a_px) * b_vy) / (b_vx * a_vy - b_vy * a_vx)
        tb = ((b_py - a_py) * a_vx - (b_px - a_px) * a_vy) / (b_vx * a_vy - b_vy * a_vx)

        if ta<0 or tb < 0:
            continue

        px = a_px + a_vx*ta
        py = a_py + a_vy*ta

        if bnd[0] <= px <= bnd[1] and bnd[0] <= py <= bnd[1]:
            p1 += 1

print(p1)

# Part 2
import sympy
# p2x + T*p2vx = Px - T*Vx
p = sympy.symbols("px, py, pz")
v = sympy.symbols("vx, vy, vz")

eqs = []
for i, (pos, vel) in enumerate(hailstones):
    t = sympy.symbols(f"t{i}")
    for j in range(3):
        eqs.append(p[j] + t*v[j] - pos[j] + t*vel[j])
    
    if i < 5:
        continue
    solutions = [solution for solution in sympy.solve(eqs)]
    if len(solutions) == 1:
        break

print(sum(solutions[0][p[i]] for i in range(3)))

