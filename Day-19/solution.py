# --- Day 19: Monster Messages ---

import re


def build_pattern(rules, start, deapth=0):
    rule = rules[start]

    if str.isalpha(rule):
        return rule

    patterns = []

    groups = list(map(lambda x: x.strip(' '), rule.split('|')))

    # by empirical evidence
    if deapth > 20:
        groups = [groups[0]]

    for group in groups:
        tokens = group.split(' ')
        pattern = ''
        for token in tokens:
            pattern += build_pattern(rules, token, deapth + 1)
        patterns.append(pattern)

    if len(patterns) > 1:
        return '(' + '|'.join(patterns) + ')'
    else:
        return patterns[0]


def run(with_cycles):
    lines = [line.strip() for line in open('input.txt')]

    arr = lines[0:lines.index('')]

    if with_cycles:
        arr.append('8: 42 | 42 8')
        arr.append('11: 42 31 | 42 11 31')

    rules = {}
    for a in arr:
        left, right = a.split(':')
        rules[left] = right.strip(' "')

    messages = lines[lines.index('') + 1:]

    pattern = build_pattern(rules, '0')
    compiled = re.compile(r'^{0}$'.format(pattern))

    valid = 0

    for message in messages:
        valid += compiled.match(message) is not None

    return valid


print("First part: ", run(with_cycles=False))
print("Second part: ", run(with_cycles=True))

