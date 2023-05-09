I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    n = I(IN()); a = inp(); aaa = []; m = -1e9
    p = a[0] // A(a[0])
    for aa in a:
        if aa // p < 0: aaa.append(m); p = -p; m = -1e9
        m = MX(aa, m)
    P(S(aaa + [m]))