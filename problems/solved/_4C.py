def f1(a, d): d[a] += 1; return f"{a}{d[a]}"
def f2(a, d): d[a] = 0; return "OK"
d = {}; b = [f1(a, d) if a in d.keys() else f2(a, d) for a in [input() for _ in range(int(input()))]]
for s in b: print(s)