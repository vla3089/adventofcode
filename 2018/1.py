#!/usr/bin/env python

from sets import Set

fname = "input1.txt"
with open(fname) as f:
    content = f.readlines()
content = [int(x) for x in content]

print("Sum is " + str(sum(content)))

seen = Set()
delta = content[0]
index = 1
length = len(content)
while delta not in seen:
    seen.add(delta)
    delta += content[index]
    index = (index + 1) % length
print delta
