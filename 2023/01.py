words = "one, two, three, four, five, six, seven, eight, nine".split(", ")
p1 = p2 = 0

f = open("inp1").readlines()
for line in f:
    parsed = ""
    for i, ch in enumerate(line):
        if ch.isdigit():
            parsed += ch
        else:
            for n, word in enumerate(words):
                j = 0
                while j < len(word) and i+j < len(line):
                    if line[i+j] == word[j]:
                        j += 1
                    else:
                        break
                if j == len(word):
                    parsed += str(n+1)

    first, last = None, None
    for ch in line:
        if ch.isdigit():
            if first == None:
                first = ch
            last = ch
    p1 += int(first+last)

    first, last = None, None
    for ch in parsed:
        if ch.isdigit():
            if first == None:
                first = ch
            last = ch
    p2 += int(first+last)

print("a", p1)
print("b", p2)

