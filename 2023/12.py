from functools import cache
lines = [line.strip().split(" ") for line in open("inp12").read().strip().split("\n")]

@cache
def dp(record, pattern, curr_pattern, record_index, pattern_index, started=False):
    if record_index == len(record):
        return pattern_index == len(pattern) or (pattern_index == len(pattern)-1 and curr_pattern == 0)
    if pattern_index == len(pattern):
        return "#" not in record[record_index:]

    curr_record = record[record_index]

    if curr_pattern < 0:
        return 0

    if curr_pattern == 0:
        if curr_record == "#":
            return 0

        if pattern_index+1 == len(pattern):
            return "#" not in record[record_index+1:]

        return dp(record, pattern, pattern[pattern_index+1], record_index+1, pattern_index+1, False)

    if curr_pattern > 0:
        if started:
            if curr_record == ".":
                return 0

            return dp(record, pattern, curr_pattern-1, record_index+1, pattern_index, True)
        else:
            if curr_record == ".":
                return dp(record, pattern, curr_pattern, record_index+1, pattern_index, False)

            if curr_record == "?":
                not_damaged = dp(record, pattern, curr_pattern, record_index+1, pattern_index, False)
                damaged = dp(record, pattern, curr_pattern-1, record_index+1, pattern_index, True)
                return not_damaged + damaged

            return dp(record, pattern, curr_pattern-1, record_index+1, pattern_index, True)

    return 0

# Part 1
p1 = 0
for record, pattern in lines:
    pattern = tuple(map(int, pattern.split(",")))
    p1 += dp(tuple(record), pattern, pattern[0], 0, 0) 

print(p1)

# Part 2
p2 = 0
for record, pattern in lines:
    pattern = tuple(map(int, pattern.split(",")))*5
    new_record = []
    for _ in range(5):
        new_record.extend(record)
        new_record.append("?")
    p2 += dp(tuple(new_record[:-1]), pattern, pattern[0], 0, 0)

print(p2)

