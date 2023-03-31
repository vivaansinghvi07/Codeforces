I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min
a, b, c = [IN() for _ in R(3)]
d = c
for e in a:
    c = c.replace(e, "", 1)
for e in b:
    c = c.replace(e, "", 1)
P("YES" if LN(c) == 0 and LN(a) + LN(b) == LN(d) else "NO")