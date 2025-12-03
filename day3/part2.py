max_joltage = lambda x: (x[1], -x[0])
output_joltage = 0

def joltage(batteries: str, digits_left: int, digits: str = '') -> int:
    if digits_left == 1:
        i, battery = max(enumerate(batteries), key=max_joltage)
        return int(digits + battery)
    else:
        i, battery = max(enumerate(batteries[:-(digits_left - 1)]), key=max_joltage)
        return joltage(batteries[i+1:], digits_left - 1, digits + battery)


with open('day3/input.txt', 'r') as f:
    for line in f:
        batteries = line.strip()
        output_joltage += joltage(batteries, 12)

print(f'The total output joltage is {output_joltage}')