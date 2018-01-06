#!/usr/bin/env python

class Stack:
  def __init__(self):
    self.__storage = []

  def isEmpty(self):
    return len(self.__storage) == 0

  def push(self,p):
    self.__storage.append(p)

  def pop(self):
    return self.__storage.pop()


score = 0
nesting_level = 0

is_garbage_mode = False
garbage_count = 0
skip_next = False

def process_in_garbage_mode(c):
    global score
    global nesting_level
    global is_garbage_mode
    global skip_next
    global garbage_count
    
    if skip_next:
        skip_next = False
    else:
        if c == '!':
            skip_next = True
        elif c == '>':
            is_garbage_mode = False
        else:
            garbage_count += 1

def process_in_group_mode(c):
    global score
    global nesting_level
    global is_garbage_mode
    global skip_next

    if c == '{':
        nesting_level += 1
        score += nesting_level
    elif c == '}':
        nesting_level -= 1
    elif c == '<':
        is_garbage_mode = True
        
def process_ch(c):
    global is_garbage_mode
    if is_garbage_mode:
        process_in_garbage_mode(c)
    else:
        process_in_group_mode(c)
                

with open('input_9.txt', 'r') as f:
    while True:
        c = f.read(1)
        if c:
            process_ch(c)
        else:
            break

print score
print garbage_count
