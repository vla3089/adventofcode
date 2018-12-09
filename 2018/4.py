#!/usr/bin/env python

from collections import defaultdict
import re

fname = "input4.txt"
# fname = "input4.test"
with open(fname) as f:
    content = f.readlines()
content = [line.strip() for line in content]


def extract(s):
    return [int(x) for x in re.findall(r'\d+', s)]


def parse_input(input):
    return sorted([extract(s) for s in input])


i = 0
sleep_time = defaultdict(int)
most_common = defaultdict(lambda: defaultdict(int))
data = parse_input(content)
while i < len(data):
    times = data[i]
    guard = times[-1]
    i += 1
    while True:
        if i >= len(data) or len(data[i]) == 6:
            break

        start = data[i][4]
        stop = data[i + 1][4]
        sleep_time[guard] += (stop - start)
        for j in range(start, stop):
            most_common[guard][j] += 1
        i += 2

_, sleepy = max(((v, k) for k, v in sleep_time.items()))
_, minute = max(((v, k) for k, v in most_common[sleepy].items()))
print(minute * sleepy)

_, sleepy, minute = max((v, guard, minute) for guard, d in most_common.items() for minute, v in d.items())
print(minute * sleepy)
