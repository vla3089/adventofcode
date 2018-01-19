#!/usr/bin/env python

with open('input_11.txt', 'r') as f:
    steps = f.readline().strip().split(',')

actions = {
    'n':  lambda (x, y): (x, y + 1),
    'ne': lambda (x, y): (x + 0.5, y + 0.5),
    'nw': lambda (x, y): (x - 0.5, y + 0.5),
    'sw': lambda (x, y): (x - 0.5, y - 0.5),
    'se': lambda (x, y): (x + 0.5, y - 0.5),
    's':  lambda (x, y): (x, y - 1)
    }

def steps_to_pos(pos):
    min_coord = min(pos)
    max_coord = max(pos)
    return max_coord - min_coord + 2 * min_coord

pos = (0, 0)
max_steps = 0
for step in steps:
    pos = actions[step](pos)
    max_steps = max(max_steps, steps_to_pos(pos))

print steps_to_pos(pos)
print max_steps
