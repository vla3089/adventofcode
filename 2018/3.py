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
    left, rest = rest.split(',', 1)
    top, rest = rest.split(':', 1)
    w, h = rest.split('x', 1)
    return (int(claim_id), int(left), int(top), int(w), int(h))
    
def inflate_claims(claims):
    grouped = collections.defaultdict(int)
    for claim in claims:
        claim_id, left, top, w, h = claim
        for i in range(left, left + w):
            for j in range(top, top + h):
                grouped[i, j] += 1
    return grouped

def overlaps_count(inflated_claims):
    return sum(1 for count in inflated_claims.values() if count > 1)

def has_no_overlaps(claim, inflated):
    claim_id, left, top, w, h = claim
    for i in range(left, left + w):
            for j in range(top, top + h):
                if inflated[i, j] != 1:
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
