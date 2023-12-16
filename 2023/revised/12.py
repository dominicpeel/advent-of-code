from functools import cache
input = open("inp12").read()

def parse_input(input):
    for line in input.splitlines():
        a, b = line.split()
        yield a, list(map(int, b.split(",")))

def solution(record, pattern):
    @cache
    def dp(curr_pattern, record_index, pattern_index):
        if record_index == len(record):
            return pattern_index == len(pattern) or (pattern_index == len(pattern)-1 and curr_pattern == 0)

        curr_record = record[record_index]

        if curr_pattern == 0:
            if curr_record == "#":
                return 0

            if pattern_index+1 == len(pattern):
                return "#" not in record[record_index+1:]

            return dp(pattern[pattern_index+1], record_index+1, pattern_index+1)

        if curr_pattern > 0:
            if curr_pattern < pattern[pattern_index]:
                if curr_record == ".":
                    return 0
                return dp(curr_pattern-1, record_index+1, pattern_index)
            else:
                if curr_record == ".":
                    return dp(curr_pattern, record_index+1, pattern_index)

                if curr_record == "?":
                    not_damaged = dp(curr_pattern, record_index+1, pattern_index)
                    damaged = dp(curr_pattern-1, record_index+1, pattern_index)
                    return not_damaged + damaged

                return dp(curr_pattern-1, record_index+1, pattern_index)

        return 0

    return dp(pattern[0], 0, 0)

# Part 1
p1 = 0
for record, pattern in parse_input(input):
    p1 += solution(record, pattern)

print(p1)

# Part 2
p2 = 0
for record, pattern in parse_input(input):
    p2 += solution("?".join(record for _ in range(5)), pattern*5)

print(p2)

