#!/usr/bin/env python

banks = []

with open('input_6.txt', 'r') as f:
    for line in f:
        line = line.strip()
        banks = map(int, line.split('\t'))

def find_major_index(banks):
    maxIndex = 0
    for i in range(len(banks)):
        if banks[i] > banks[maxIndex]:
            maxIndex = i
    return maxIndex

history = dict()
size = len(banks)
cycles = 0

while (not str(banks) in history):
    history[(str(banks))] = cycles
    cycles += 1
    index = find_major_index(banks)
    redistributed = banks[index]
    banks[index] = 0
    index += 1
    while (redistributed > 0):
        banks[index % size] += 1
        redistributed -= 1
        index += 1

print "1st: " + str(cycles)
print "2nd: " + str(cycles - history[str(banks)])
