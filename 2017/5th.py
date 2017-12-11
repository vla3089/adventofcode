#!/usr/bin/env python

trampolines = []

with open('input_5.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            trampolines.append(int(line))


steps = 0
pc = 0

while (0 <= pc < len(trampolines)):
    steps += 1
    jump = trampolines[pc]
    trampolines[pc] = trampolines[pc] + 1
    pc += jump
            
print steps
