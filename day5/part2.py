with open("day5/input.txt", "r") as f:
    content = f.read()
    sections = content.split("\n\n")

    ranges = [tuple(map(int, l.split("-"))) for l in sections[0].splitlines()]
    # ids = [int(l) for l in sections[1].splitlines()]

    bounds = [(b[0], 1) for b in ranges] + [(b[1], -1) for b in ranges]
    bounds = sorted(bounds, key=lambda r: r[0])

    open_counts: list[tuple[int, int]] = []
    parens = 0

    for bound, delta in bounds:
        parens += delta
        open_counts.append((bound, parens))
    
    num_fresh = 0
    for b, prev in zip(open_counts[1:], open_counts):
        if prev[1] > 0:
            delta = b[0] - prev[0]
            if b[1] == 0:
                delta += 1
            num_fresh += delta
        
    print(num_fresh)
