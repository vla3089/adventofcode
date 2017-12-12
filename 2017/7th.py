#!/usr/bin/env python

parts = {}

with open('input_7.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            partition = line.partition(" -> ")
            header = partition[0].split(" (")
            weight = int(header[1][:-1])
            if len(partition[2]) > 0:
                children = map(str.strip, partition[2].split(','))
            else:
                children = []
            parts.update({header[0] : (weight, children)}) 

def find_parent_key(child_head, parts):
    for key, value in parts.iteritems():
        for child_key in value[1]:
            if child_head == child_key:
                return key
    return None

def find_tree_bottom_header(parts):
    currBottomKey = parts.keys()[0]
    while True:
        parent = find_parent_key(currBottomKey, parts)
        if parent == None:
            return currBottomKey
        currBottomKey = parent


bottomHeader = find_tree_bottom_header(parts)
print bottomHeader

################################# task 2

class ValidationError(Exception):
    def __init__(self, message, head, weight_diff):
        super(ValidationError, self).__init__(message)
        self.head = head
        self.weight_diff = weight_diff

def validate_disk_weight(parts, children):
    length = len(children)
    if (length < 3):
        return 0
    first = parts[children[0]][0]
    second = parts[children[1]][0]
    third = parts[children[2]][0]
    if (first == second) and (first == third):
        return None
    elif second == third:
        raise ValidationError('Disk is unbalanced', children[0], second - first)
    elif first == second:
        raise ValidationError('Disk is unbalanced', children[2], second - third)
    else:
        raise ValidationError('Disk is unbalanced', children[1], first - second)

def validate_tree(parts, head):
    (weight,children) = parts[head]

    if (len(children) <= 0):
        return
    for child_head in children:
        validate_tree(parts, child_head)
    validate_disk_weight(parts, children)
    items_count = len(children)
    item_weight = parts[children[0]][0]
    parts.update({head : (weight + item_weight * items_count, [])})

try:
    validate_tree(dict(parts), bottomHeader)
except ValidationError as error:
    defined_weight = parts[error.head][0]
    correct_weight = defined_weight + error.weight_diff
    print correct_weight
