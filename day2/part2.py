total = 0

def recursive_is_invalid(s: str, l: int) -> bool:
    if l*2 == len(s):
        return s[:l] == s[l:]
    elif l*2 > len(s):
        return False
    else:
        return s[:l] == s[l:l*2] and recursive_is_invalid(s[l:], l)

def is_invalid(n: int) -> bool:
    s = str(n)
    for i in range(1, (len(s) // 2) + 1):
        if recursive_is_invalid(s, i):
            return True
    return False

with open('day2/input.txt') as f:
    line = f.readline()
    for r in line.split(','):
        start, end = map(int, r.split('-'))
        for n in range(start, end+1):
            s = str(n)
            if is_invalid(n):
                total += n

print(f'The sum of all the invalid IDs is {total}')