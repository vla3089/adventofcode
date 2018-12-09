#!/usr/bin/env python

from collections import defaultdict


# 000000000111111111122222222222333333333344444444
# 123456789012345678901234567890123456789012345678
# Step G must be finished before step X can begin.
def parse_line(input_line):
    return input_line[5], input_line[36]


def parse_input(content):
    return [parse_line(line) for line in content]


def get_yet_unavailable(requirements):
    unavailable_yet = set()
    for required_step, for_steps in requirements.iteritems():
        for step in for_steps:
            unavailable_yet.add(step)
    return unavailable_yet


def task1(steps):
    backlog = set()
    requirements = defaultdict(list)
    for required_step, for_step in steps:
        backlog.add(required_step)
        backlog.add(for_step)
        requirements[required_step].append(for_step)
    instruction = ""
    while backlog:
        unavailable_yet = get_yet_unavailable(requirements)
        as_list = sorted(list(backlog.difference(unavailable_yet)))
        next_step, _ = as_list[0], set(as_list[1:])
        backlog.discard(next_step)
        instruction += next_step
        requirements.pop(next_step, None)

    return instruction


def task2(steps, workers, initial_step_work):
    backlog = set()
    requirements = defaultdict(list)
    unavailable_yet = set()
    for required_step, for_step in steps:
        backlog.add(required_step)
        backlog.add(for_step)
        requirements[required_step].append(for_step)
        unavailable_yet.add(for_step)
    assigned = set()  # (Step, Accomplish Time)
    time = 0

    while backlog or assigned:
        accomplished = set([step for step, accomplish_time in assigned if accomplish_time <= time])
        assigned = set([(step, accomplish_time) for step, accomplish_time in assigned if accomplish_time > time])
        if accomplished:
            for accomplished_item in accomplished:
                requirements.pop(accomplished_item, None)
            unavailable_yet = get_yet_unavailable(requirements)
            backlog = backlog.difference(accomplished)
        tmp = set([step for step, _ in assigned])
        steps_to_go = sorted(list(backlog.difference(unavailable_yet).difference(tmp)))
        while len(assigned) < workers and len(steps_to_go) > 0:
            next, steps_to_go = steps_to_go[0], steps_to_go[1:]
            assigned.add((next, time + initial_step_work + ord(next) - ord('A') + 1))
        time += 1
    return time - 1


# print task1(parse_input(open("input7.test").readlines()))
print task1(parse_input(open("input7.txt").readlines()))

# print task2(parse_input(open("input7.test").readlines()), 2, 0)
print task2(parse_input(open("input7.txt").readlines()), 5, 60)
