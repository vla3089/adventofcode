#!/usr/bin/env python


valid_1 = 0

with open('input_4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            mywords = line.split(" ")
            myset = set(mywords)
            if len(myset) == len(mywords):
                valid_1 += 1

print valid_1

valid_2 = 0

with open('input_4.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            words = map(''.join, map(sorted, line.split(" ")))
            myset = set(words)
            if len(myset) == len(words):
                valid_2 += 1

print valid_2
