#!/usr/bin/env python

size = 256

with open('input_10.txt', 'r') as f:
    input = f.readline().strip()

def knot_hash_round(arr, start, end):
    size = len(arr)
    while start < end:
        ns = start % size
        ne = end % size
        arr[ns], arr[ne] = arr[ne], arr[ns]
        start += 1
        end -= 1
    
def knot_hash(arr, input, rounds):
    skip_size = 0
    cp = 0
    list = range(0, size)
    for round in xrange(rounds):
        for item in input:
            start = cp
            end = cp + item - 1
            knot_hash_round(arr, start, end)
            cp = (cp + item + skip_size) % size
            skip_size += 1
    return arr
   
def slice(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr = arr[size:]
     arrs.append(arr)
     return arrs

def first_task(input):
    lengths = map(int, input.split(','))
    arr = knot_hash(range(0, size), lengths, 1)
    print arr[0] * arr[1]

import operator

def sparse_to_dense_hash(sparse_hash):
    dense_hash = slice(sparse_hash, 16)
    dense_hash = [reduce(operator.xor, i) for i in dense_hash]
    dense_hash = ['{0:02x}'.format(item) for item in dense_hash]
    return ''.join(map(str,dense_hash))

def second_task(input):
    lengths = map(ord, input) + [17, 31, 73, 47, 23]
    sparse_hash = knot_hash(range(0, size), lengths, 64)
    print sparse_to_dense_hash(sparse_hash)

first_task(input)
second_task(input)
