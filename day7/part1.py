with open('day7/input.txt') as f:
    lines = f.read().splitlines()

n = len(lines[0])
beams: set[int] = set([lines[0].index('S')])

count = 0

for l in lines[1:]:
    next_beams: set[int] = set()
    splitters = set([i for i, s in enumerate(l) if s == '^'])

    for b in beams:
        if b in splitters:
            count += 1
            if b-1 >= 0:
                next_beams.add(b-1)
            if b+1 < n:
                next_beams.add(b+1)
        else:
            next_beams.add(b)
    
    beams = next_beams

print(count)