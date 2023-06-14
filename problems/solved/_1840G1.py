c, f, d = [False] * (1_000_001), [0] * 1_000, 0
def s(a):
    global c, f, d
    for i in range(1000):
        n = int(input())
        if c[n]: exit(print(f"! {d - f.index(n)}", flush=True))
        if a == 1: f[i] = n
        c[n] = True; d += a; print(f"+ {a}", flush=True)
s(1); s(1000)