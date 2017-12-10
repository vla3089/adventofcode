#!/usr/bin/env python

checksum = 0

with open('input_2.1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            numbers = map(int, line.split('\t'))
            checksum += (max(numbers) - min(numbers))

print checksum

