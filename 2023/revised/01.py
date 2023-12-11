words = "one, two, three, four, five, six, seven, eight, nine".split(", ")
p1 = p2 = 0

f = open("../inp1").readlines()
for line in f:
    parsed = ""
    for i, ch in enumerate(line):
        if ch.isdigit():
            parsed += ch
        else:
            for n, word in enumerate(words):
                if line[i:].startswith(word):
                    parsed += str(n+1)

    digits = [ch for ch in line if ch.isdigit()]
    p1 += int(digits[0] + digits[-1])
    digits = [ch for ch in parsed if ch.isdigit()]
    p2 += int(digits[0] + digits[-1])

print("a", p1)
print("b", p2)

