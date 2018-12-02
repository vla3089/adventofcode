#!/usr/bin/env python

import collections

fname = "input2.txt"
with open(fname) as f:
    content = f.readlines()
content = [line.strip() for line in content]

def distance(line1, line2):
    to = min(len(line1), len(line2))
    distance = 0
    last_diff_index = 0
    for x in range(0, to):
        if (line1[x] != line2[x]):
            distance += 1
            last_diff_index = x
    return (distance, last_diff_index)

twos = 0
threes = 0
for line in content:
    grouped = collections.Counter(line)
    inv = {v: k for k, v in grouped.iteritems()}
    if 2 in inv:
        twos += 1
    if 3 in inv:
        threes += 1

print twos * threes

def part2():
    hasher = set()
    for line in content:
        for i, _ in enumerate(line):
            key = (line[:i], line[i+1:])
            if key in hasher:
                return key[0] + key[1]
            hasher.add(key)
print part2()
            
#for x in range(0, len(content)):
#    for y in range(x + 1, len(content)):
#        line = content[x]
#        dist = distance(line, content[y])
#        if dist[0] == 1:
#            print line[:dist[1]] + line[dist[1] + 1:]
