#!/usr/bin/env python

checksum = 0

with open('input_2.1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            numbers = map(int, line.split('\t'))
            for x in numbers:
                for y in numbers:
                    if (x != y):
                        if (x % y == 0):
                            checksum = checksum + x / y

print checksum

