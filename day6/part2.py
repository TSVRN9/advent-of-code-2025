import operator
from functools import reduce
from typing import Callable

operations = {
    '+': operator.add,
    '*': operator.mul
}

with open('day6/input.txt', 'r') as f:
    lines = f.read().splitlines()

problems: list[list[int]] = []
ops: list[Callable[[int, int], int]] = []

current_problem = []
for j in reversed(range(len(lines[0]))):
    current_number = ''
    for i in range(len(lines)):
        ch = lines[i][j]
        if ch in '+*':
            ops.append(operations[ch])
            current_problem.append(int(current_number))
            problems.append(current_problem)

            current_number = ''
            current_problem = []
        elif ch != ' ':
            current_number += ch
    if current_number != '':
        current_problem.append(int(current_number))
        current_number = ''
        


total = 0
for p, op in zip(problems, ops):
    total += reduce(op, p)

print(total)