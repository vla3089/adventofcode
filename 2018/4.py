#!/usr/bin/env python

import collections

fname = "input4.txt"
# fname = "input4.test"
with open(fname) as f:
    content = f.readlines()
content = [line.strip() for line in content]


def strip_guard(descr):
    return descr.replace(" begins shift", "")


# 000000000011111111
# 012345678901234567
# [1518-07-28 00:10] falls asleep
def parse_line(line):
    month = int(line[6:8])
    day = int(line[9:11])
    hours = int(line[12:14])
    mins = int(line[15:17])
    as_mins = month * 43830 + day * 1440 + hours * 60 + mins
    descr = strip_guard(line[19:])
    return (as_mins, month, day, mins, descr)


def parse_input(input):
    parsed = [parse_line(line) for line in input]
    parsed.sort(key=lambda item: item[0])
    parsed = [(month, day, mins, descr) for _, month, day, mins, descr in parsed]
    return parsed


def make_date_string(month, day):
    return '{:02d}-{:02d}'.format(month, day)


def merge_asleeps_awakes(asleeps, awakes):
    merged = zip(asleeps, awakes)
    merged = [(make_date_string(asleepItem[0], asleepItem[1]),
               awakeItem[2] - asleepItem[2],
               (asleepItem[2], awakeItem[2])) for asleepItem, awakeItem
              in merged]
    return merged


parsed = parse_input(content)


def group_by_guard_and_day(parsed):
    guards = []
    guard = None
    asleeps = []
    awakes = []
    for month, day, mins, command in parsed:
        if "Guard" in command:
            if guard is not None:
                guards.append((guard, merge_asleeps_awakes(asleeps, awakes)))
                asleeps = []
                awakes = []
            guard = command
        elif "asleep" in command:
            asleeps.append((month, day, mins))
        elif "wakes" in command:
            awakes.append((month, day, mins))
    guards.append((guard, merge_asleeps_awakes(asleeps, awakes)))
    return guards


def inflate_minutes(group_by_guard_and_day):
    merged = collections.defaultdict(list)
    for guard, wakes in group_by_guard_and_day:
        for date, duration, period in wakes:
            merged[(date, guard)] = merged[(date, guard)] + list(range(period[0], period[1]))
    return merged


def group_by_freqency(inflated):
    freq = collections.defaultdict(dict)
    for key, minutes_asleep in inflated.iteritems():
        freq[key[1]] = collections.defaultdict(int)
    for key, minutes_asleep in inflated.iteritems():
        for minute in minutes_asleep:
            freq[key[1]][minute] += 1
    return freq


def group_by_guard_and_by_day2(inflated):
    minutes_during_a_day = collections.defaultdict(dict)
    for key, value in inflated.iteritems():
        minutes_during_a_day[key[1]] = collections.defaultdict(list)
    for key, value in inflated.iteritems():
        minutes_during_a_day[key[1]][key[0]] = minutes_during_a_day[key[1]][key[0]] + value
    return minutes_during_a_day


def minutes_asleep_during_a_day(grouped_by_guard_and_by_day2):
    grouped = collections.defaultdict(list)
    for guard, day_dict in grouped_by_guard_and_by_day2.iteritems():
        for day, minutes_asleep in day_dict.iteritems():
            grouped[guard].append((day, len(minutes_asleep)))
    return grouped


def minutes_asleep(minutes_asleep_during_a_day):
    grouped = collections.defaultdict(list)
    for guard, day_arr in minutes_asleep_during_a_day.iteritems():
        grouped[guard] = sum([pair[1] for pair in day_arr])
    return grouped


def guard_with_max_minutes_asleep(minutes_asleep):
    return max(minutes_asleep.iteritems(), key=lambda item: item[1])[0]


def group_guard_by_freq(grouped_by_guard_and_by_day2, guard):
    data = grouped_by_guard_and_by_day2[guard]
    grouped = collections.defaultdict(int)
    for key, value in data.iteritems():
        for minute in value:
            grouped[minute] += 1
    return grouped


def max_frequency(grouped_guard_by_freq):
    return max(grouped_guard_by_freq.iteritems(), key=lambda item: item[1])


inflated = inflate_minutes(group_by_guard_and_day(parsed))

grouped_by_guard_and_by_day2 = group_by_guard_and_by_day2(inflated)
guard_with_max_minutes_asleep = guard_with_max_minutes_asleep(
    minutes_asleep(minutes_asleep_during_a_day(grouped_by_guard_and_by_day2)))
max_frequency_minute = max_frequency(group_guard_by_freq(grouped_by_guard_and_by_day2, guard_with_max_minutes_asleep))[
    0]
print "Task 1 = {}".format(int(guard_with_max_minutes_asleep[7:]) * int(max_frequency_minute))

max_guard_freq = {}
for guard, dict in grouped_by_guard_and_by_day2.iteritems():
    max_guard_freq[guard] = max_frequency(group_guard_by_freq(grouped_by_guard_and_by_day2, guard))

max_guard_freq = [(guard, minute_and_count[0], minute_and_count[1]) for guard, minute_and_count in
                  max_guard_freq.iteritems()]
max_guard_freq = max(max_guard_freq, key=lambda item: item[2])
print "Task 2 = {}".format(int(max_guard_freq[0][7:]) * int(max_guard_freq[1]))
