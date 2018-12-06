#!/usr/bin/env python

from collections import defaultdict

fname = "input6.txt"
threshold = 10000
with open(fname) as f:
    content = f.readlines()
content = [line.split(',') for line in content]
content = [(int(line[0]), int(line[1])) for line in content]

minX = min(content, key=lambda item: item[0])[0]
maxX = max(content, key=lambda item: item[0])[0]

minY = min(content, key=lambda item: item[1])[1]
maxY = max(content, key=lambda item: item[1])[1]


def reverse_dict(d):
    rev = defaultdict(list)
    for key, value in d.iteritems():
        rev[value].append(key)
    return rev


def calc_manhattan_distance(x1, x2, y1, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def calculate_distance_to_point(coords, x, y):
    return {k: calc_manhattan_distance(k[0], x, k[1], y) for k in coords}


def find_closest_area(areas, x, y):
    a = calculate_distance_to_point(areas, x, y)
    rev = reverse_dict(a)
    closest = sorted(rev.items(), key=lambda item: item[0])[0]
    if len(closest[1]) == 1:
        return closest[0], closest[1][0]
    else:
        return None


def sum_distances_to_point(areas, x, y):
    return sum(calculate_distance_to_point(areas, x, y).values())


infinite = set()
for x in range(minX, maxX):
    closest = find_closest_area(content, x, minY - 1)
    if closest is not None:
        infinite.add(closest[1])

for x in range(minX, maxX):
    closest = find_closest_area(content, x, maxY + 1)
    if closest is not None:
        infinite.add(closest[1])

for y in range(minY, maxY):
    closest = find_closest_area(content, minX - 1, y)
    if closest is not None:
        infinite.add(closest[1])

for y in range(minY, maxY):
    closest = find_closest_area(content, maxX + 1, y)
    if closest is not None:
        infinite.add(closest[1])


areas = defaultdict(int)
for x in range(minX, maxX):
    for y in range(minY, maxY):
        closest = find_closest_area(content, x, y)
        if closest is not None:
            distance, key = closest
            areas[key] += 1

areas = {k: v for k, v in areas.iteritems() if k not in infinite}
print max(areas.iteritems(), key=lambda item: item[1])[1]

def task2(coords, centerX, centerY, threshold):
    minX = centerX
    maxX = centerX
    minY = centerY
    maxY = centerY

    center_sum = sum_distances_to_point(coords, centerX, centerY)
    if center_sum < threshold:
        region_sum = 1
    else:
        region_sum = 0
    minX -= 1
    maxX += 1
    minY -= 1
    maxY += 1

    while True:
        top_edge = [sum_distances_to_point(coords, x, minY) for x in range(minX, maxX + 1)]  # top edge
        bottom_edge = [sum_distances_to_point(coords, x, maxY) for x in range(minX, maxX + 1)]  # bottom edge
        left_edge = [sum_distances_to_point(coords, minX, y) for y in range(minY + 1, maxY)]  # left edge
        right_edge = [sum_distances_to_point(coords, maxX, y) for y in range(minY + 1, maxY)]  # right edge
        region = top_edge + bottom_edge + left_edge + right_edge
        region = [dist for dist in region if dist < threshold]
        if len(region) != 0:
            region_sum += len(region)
            minX -= 1
            maxX += 1
            minY -= 1
            maxY += 1
        else:
            return region_sum


centerX = (minX + maxX) / 2
centerY = (minY + maxY) / 2


print task2(content, centerX, centerY, threshold)
