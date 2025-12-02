total = 0

with open('day2/input.txt') as f:
    line = f.readline()
    for r in line.split(','):
        start, end = map(int, r.split('-'))
        for i in range(start, end+1):
            s = str(i)
            half = len(s) // 2
            if s[:half] == s[half:]:
                total += i

print(f'The sum of all the invalid IDs is {total}')