inp_workflows, parts = [x.split("\n") for x in open("inp19").read().strip().split("\n\n")]

workflows = {}

for workflow in inp_workflows:
    key, conditions = workflow[:-1].split("{") # }
    workflows[key] = []

    for condition in conditions.split(","):
        condition = condition.split(":")
        if len(condition) == 2:
            workflows[key].append(condition)
        else:
            workflows[key].append(["True", condition[0]])

p1 = 0
x=m=a=s=0
for part in parts:
    for cat in part[1:-1].split(","):
        exec(cat)

    curr = "in"
    while curr not in ("A", "R"):
        for condition in workflows[curr]:
            if eval(condition[0]):
                curr = condition[1]
                break 

    p1 += x+m+a+s if curr == "A" else 0

print(p1)

p2 = 0
xmas = {k:v for v,k in enumerate("xmas")}
def dfs(curr, rs=[[1,4000], [1,4000], [1,4000], [1,4000]]):
    rs = [[a,b] for a,b in rs]
    global p2
    if curr in ("A", "R"):
        res = 1
        for a,b in rs:
            res *= b-a+1
        p2 += res if curr == "A" else 0
        return 

    for condition, key in workflows[curr][:-1]:
        cat, val = condition.replace(">","<").split("<")
        index = xmas[cat]
        a,b = rs[index]
        symbol = condition[1]
        if symbol == "<":
            rs[index] =  [a,int(val)-1]
            dfs(key, rs)
            rs[index] = [int(val),b]
        else:
            rs[index] = [int(val)+1, b]
            dfs(key, rs)
            rs[index] = [a, int(val)]

    dfs(workflows[curr][-1][-1], rs)

dfs("in")
print(p2)

