from collections import defaultdict

with open("day7/input.txt") as f:
    lines = f.read().splitlines()

beams: defaultdict[int, int] = defaultdict(int)
beams[lines[0].index("S")] = 1

for l in lines[1:]:
    next_beams: defaultdict[int, int] = defaultdict(int)
    splitters = set([i for i, s in enumerate(l) if s == "^"])

    for b in beams.keys():
        n = beams[b]
        if b in splitters:
            if b - 1 >= 0:
                next_beams[b-1] += n
            if b + 1 < len(lines[0]):
                next_beams[b+1] += n
        else:
            next_beams[b] += n
    beams = next_beams

print(sum(beams.values()))