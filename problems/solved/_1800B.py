I, IN, M, R, LN, LS = int, input, map, range, len, list
al = "abcdefghijklmnopqrstuvwxyz"
for _ in R(I(IN())):
    n, k = M(I, IN().split(" "))
    s, cs = IN(), {}
    t = 0
    r = 0
    for c in al:
        cs[c] = cs[c.upper()] = 0
    for c in s:
        cs[c] += 1
    for c in al:
        try:
            x = (cs[c] + cs[c.upper()]) // 2
            t += x
            r += min(abs(cs[c] - x), abs(cs[c.upper()] - x))
        except:
            continue
    r -= min(r, k)
    print(t-r)