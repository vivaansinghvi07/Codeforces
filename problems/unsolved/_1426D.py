m, s, n, a, t = {0: 0}, 0, int(input()), [*map(int, input().split())], 0
for i, j in enumerate(a):
    s += j
    if (v:=m.get(s, None)) is not None:
        try:
            if lp[1] > v:
                t -= 1
        except: pass
        t += 1
        lp = (v, i)
    m[s] = i + 1
    try: print(t, s, lp)
    except: pass
print(t)