#!/usr/bin/env python

fname = "input5.txt"
with open(fname) as f:
    content = f.readlines()
content = content[0].strip()


def is_different_register(ch1, ch2):
    return (ch1.islower() and ch2.isupper()) or (ch1.isupper() and ch2.islower())


def is_polymer_unit(ch1, ch2):
    return (ch1.lower() == ch2.lower()) and is_different_register(ch1, ch2)


def reduce_polymer(polymer):
    index = 0
    while index < len(polymer) - 1:
        chain_end_index = index
        if is_polymer_unit(polymer[chain_end_index], polymer[chain_end_index + 1]):
            polymer = "".join([polymer[:index], polymer[chain_end_index + 2:]])
            if index > 0:
                index -= 1
        else:
            index += 1
    return polymer


print len(reduce_polymer(content))

alphabet = list(map(chr, range(97, 123)))
improved = [content.replace(letter, "").replace(letter.upper(), "") for letter in alphabet]
improved = [len(reduce_polymer(item)) for item in improved]
print min(improved)
