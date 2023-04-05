I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    a, i = [], IN()
    for l in R(LN(i)):
        d = int(i[l]) * 10 ** (LN(i) - l - 1)
        if d:
            a.append(d)
    P(LN(a))
    for l in a:
        P(l, end=" ")
    P()