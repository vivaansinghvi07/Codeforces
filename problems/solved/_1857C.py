from collections import Counter
class Node: 
    def __init__(self, d, n): self.data, self.next = d, n
for _ in range(int(input())):
    n, d, c, e = int(input()), dict(Counter(map(int, input().split()))), 1, []
    a = sorted([*d.items()], key=lambda x: x[0])
    for ii, (i, c) in enumerate(a): t = Node((i, c), None if ii == 0 else t)
    while t is not None:
        if t.data[1] != c:
            s = Node((t.data[0], t.data[1]-c), t.next)
            t.next = s
            e.append(t.data[0])
        t, c = t.next, c + 1
    print(*e, *d.keys(), 1_000_000_000)