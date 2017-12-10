#!/usr/bin/env python


valid = 0

with open('input_4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            mywords = line.split(" ")
            myset = set(mywords)
            if len(myset) == len(mywords):
                valid += 1

print valid
