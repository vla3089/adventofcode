#!/usr/bin/env python

def task1(input):
    meta_sum = 0
    stack = []
    tail = input
    while tail or stack:
        if stack:
            child_nodes, meta_entries = stack.pop()
            if child_nodes == 0:
                for i in range(meta_entries):
                    meta_sum += tail[i]
                tail = tail[meta_entries:]
            else:
                stack.append((child_nodes - 1, meta_entries))
                child_nodes, meta_entries, tail = tail[0], tail[1], tail[2:]
                stack.append((child_nodes, meta_entries))
        else:
            child_nodes, meta_entries, tail = tail[0], tail[1], tail[2:]
            stack.append((child_nodes, meta_entries))
    return meta_sum


print task1([int(x) for x in open("input8.test").readline().split(" ")])
print task1([int(x) for x in open("input8.txt").readline().split(" ")])
