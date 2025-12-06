import re
import operator
from functools import reduce

operations = {
    '+': operator.add,
    '*': operator.mul
}

with open('day6/input.txt', 'r') as f:
    lines = f.read().splitlines()

tokens = [filter(lambda l: len(l) != 0, re.split(' +', l)) for l in lines]

nums = [list(map(int, l)) for l in tokens[:-1]]
problems = [list(l) for l in zip(*nums)] # transpose
ops = [operations[s] for s in tokens[-1]]

total = 0
for n, op in zip(problems, ops):
    total += reduce(op, n)

print(total)