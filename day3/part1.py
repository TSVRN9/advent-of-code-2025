max_joltage = lambda x: (x[1], -x[0])
output_joltage = 0

with open('day3/input.txt', 'r') as f:
    for line in f:
        joltages = list(enumerate(line.strip()))
        i, first = max(joltages[:-1], key=max_joltage)
        _, second = max(joltages[i+1:], key=max_joltage)
        output_joltage += int(first + second)

print(f'The total output joltage is {output_joltage}')