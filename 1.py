words = "one, two, three, four, five, six, seven, eight, nine".split(", ")
resA = resB = 0

f = open("inp").readlines()
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
    resA += int(first+last)

    first, last = None, None
    for ch in parsed:
        if ch.isdigit():
            if first == None:
                first = ch
            last = ch
    resB += int(first+last)

print("a", resA)
print("b", resB)

