#!/usr/bin/env python

def task1(input):
    meta_sum = 0
    stack = []
    pos = 0
    while pos < len(input) or stack:
        if stack:
            child_nodes, meta_entries = stack.pop()
            if child_nodes == 0:
                for i in range(pos, pos + meta_entries):
                    meta_sum += input[i]
                pos += meta_entries
            else:
                stack.append((child_nodes - 1, meta_entries))
                child_nodes, meta_entries = input[pos], input[pos + 1]
                pos += 2
                stack.append((child_nodes, meta_entries))
        else:
            child_nodes, meta_entries = input[pos], input[pos + 1]
            pos += 2
            stack.append((child_nodes, meta_entries))
    return meta_sum


print task1([int(x) for x in open("input8.test").readline().split(" ")])
print task1([int(x) for x in open("input8.txt").readline().split(" ")])
