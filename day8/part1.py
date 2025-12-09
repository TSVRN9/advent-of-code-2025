import numpy as np
from collections import defaultdict as D
from scipy.spatial.distance import pdist
from math import prod

points = np.loadtxt("day8/input.txt", dtype=np.intp, delimiter=",")
n = len(points)
distances = pdist(points)
sorted_indices = np.argsort(distances)
index_pairs = np.array(np.triu_indices(n, k=1)).T
sorted_pairs = index_pairs[sorted_indices]

circuits: D[int, set[int]] = D(set)

for a, b in sorted_pairs[:1000]:
    A = circuits[a]
    B = circuits[b]

    A.add(a)
    B.add(b)

    if A != B:
        C = A | B
        circuits.update({n: C for n in C})

sets = {frozenset(s) for s in circuits.values()}
circuit_lengths = sorted([len(s) for s in sets], reverse=True)
product = prod(circuit_lengths[:3])

print(product)
