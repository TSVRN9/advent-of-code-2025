from bisect import bisect_left

with open("day5/input.txt", "r") as f:
    content = f.read()
    sections = content.split("\n\n")

    ranges = [tuple(map(int, l.split("-"))) for l in sections[0].splitlines()]
    ids = [int(l) for l in sections[1].splitlines()]

    bounds = [(b[0], 1) for b in ranges] + [(b[1], -1) for b in ranges]
    bounds = sorted(bounds, key=lambda r: r[0])

    open_counts: list[tuple[int, int]] = []
    parens = 0

    for bound, delta in bounds:
        parens += delta
        open_counts.append((bound, parens))

    print(open_counts)
    
    num_fresh = 0
    for i in ids:
        idx = bisect_left(open_counts, i, key=lambda b: b[0]) - 1
        if idx >= 0 and idx < len(open_counts):
            _, num_open = open_counts[idx]

            if num_open > 0:
                print(f'{i}, {idx}')
                num_fresh += 1
    
    print(num_fresh)
