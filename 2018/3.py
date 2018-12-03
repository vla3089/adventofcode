#!/usr/bin/env python

import collections

fname = "input3.txt"
with open(fname) as f:
    content = f.readlines()
content = [line.strip() for line in content]

# claim contract
# #1 @ 432,394: 29x14
def parse_claim(claim):
    claim = claim[1:]
    claim_id, rest = claim.split('@', 1)
    x, rest = rest.split(',', 1)
    y, rest = rest.split(':', 1)
    w, h = rest.split('x', 1)
    return (int(claim_id), int(x), int(y), int(w), int(h))
    
def inflate_claims(claims):
    grouped = {}
    for claim in claims:
        claim_id, x, y, w, h = claim
        for i in range(0, w):
            for j in range(0, h):
                key = (x + i, y + j)
                if key in grouped:
                    grouped[key] += 1
                else:
                    grouped[key] = 1
    return grouped

def overlaps_count(inflated_claims):
    return len({k:v for k, v in inflated_claims.iteritems() if v > 1})

def has_no_overlaps(claim, inflated):
    claim_id, x, y, w, h = claim
    for i in range(0, w):
            for j in range(0, h):
                key = (x + i, y + j)
                if inflated[key] != 1:
                    return False
    return True

def first_no_overlap_claim(claims, inflated):
    for claim in claims:
        if has_no_overlaps(claim, inflated):
            return claim
    return None

claims = [parse_claim(claim) for claim in content]
inflated = inflate_claims(claims)

print overlaps_count(inflated)

not_overlapped = first_no_overlap_claim(claims, inflated)
print not_overlapped[0]
