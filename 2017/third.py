#!/usr/bin/env python

input = 368078

size = 1
s_size = size * size # squared size
while (s_size < input):
    size += 2
    s_size = size * size

bottom_right = s_size
bottom_left = s_size - size + 1
top_left = s_size - 2 * size + 2
top_right = s_size - 3 * size + 3

input_x = -1
input_y = -1

# bottom horizontal line
if (input > bottom_left):
    input_x = size - 1
    input_y = input - bottom_left
elif (input > top_left):
    input_y = input - top_left
    input_x = 0
elif (input > top_right):
    input_x = 0
    input_y = size - input + top_right - 1
else:
    input_x = top_right - input
    input_y = size - 1
    
ap_x = size / 2
ap_y = ap_x

print abs(ap_x - input_x) + abs(ap_y - input_y)
