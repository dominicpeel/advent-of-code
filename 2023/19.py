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
x = m = a = s = 0
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
def dfs(curr, x=(1,4000), m=(1,4000), a=(1,4000), s=(1,4000)):
    global p2
    if workflow in ("A", "R"):
        p2 += (x[1]-x[0])*(m[1]-m[0])*(a[1]-a[0])*(s[1]-s[0]) if workflow == "A" else 0

    for condition, key in workflows[curr][:-1]:
        print(condition[0])

    # otherwise condition
    # dfs(workflows[curr][-1][-1])


dfs("in")

